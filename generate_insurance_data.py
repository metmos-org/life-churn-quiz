import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
n_customers = 10000
churn_rate = 0.15
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 1, 1)

# Helper functions
def generate_date_between(start, end):
    """Generate random date between start and end"""
    days_between = (end - start).days
    random_days = random.randint(0, days_between)
    return start + timedelta(days=random_days)

def generate_customer_info(n_customers):
    """Generate customer demographic data"""
    data = {
        'customer_id': [f'CUST_{i:06d}' for i in range(1, n_customers + 1)],
        'age': np.random.normal(45, 12, n_customers).clip(25, 75).astype(int),
        'gender': np.random.choice(['M', 'F'], n_customers, p=[0.52, 0.48]),
        'marital_status': np.random.choice(['Single', 'Married', 'Divorced', 'Widowed'], 
                                         n_customers, p=[0.25, 0.55, 0.15, 0.05]),
        'dependents': np.random.poisson(1.5, n_customers).clip(0, 6),
        'income_bracket': np.random.choice(['Low', 'Medium', 'High', 'VeryHigh'], 
                                         n_customers, p=[0.15, 0.45, 0.30, 0.10]),
        'employment_status': np.random.choice(['Employed', 'Self-employed', 'Retired', 'Unemployed'], 
                                            n_customers, p=[0.65, 0.20, 0.12, 0.03]),
        'education_level': np.random.choice(['HighSchool', 'Bachelor', 'Master', 'PhD'], 
                                          n_customers, p=[0.30, 0.45, 0.20, 0.05])
    }
    return pd.DataFrame(data)

def generate_policy_data(customer_df):
    """Generate policy information"""
    n_customers = len(customer_df)
    
    # Policy amount influenced by income bracket
    income_to_coverage = {
        'Low': (50000, 150000),
        'Medium': (100000, 300000),
        'High': (250000, 750000),
        'VeryHigh': (500000, 2000000)
    }
    
    policy_amounts = []
    for income in customer_df['income_bracket']:
        min_amt, max_amt = income_to_coverage[income]
        amount = np.random.uniform(min_amt, max_amt)
        # Round to nearest 50k
        amount = round(amount / 50000) * 50000
        policy_amounts.append(amount)
    
    # Premium calculation (simplified: based on age and coverage)
    base_rate = 0.002  # 0.2% of coverage as base annual premium
    age_factor = 1 + (customer_df['age'] - 30) * 0.02  # 2% increase per year over 30
    annual_premiums = np.array(policy_amounts) * base_rate * age_factor
    monthly_premiums = annual_premiums / 12
    
    data = {
        'customer_id': customer_df['customer_id'],
        'policy_type': np.random.choice(['Term', 'Whole', 'Universal'], 
                                      n_customers, p=[0.60, 0.30, 0.10]),
        'policy_start_date': [generate_date_between(start_date, end_date - timedelta(days=90)) 
                            for _ in range(n_customers)],
        'policy_amount': policy_amounts,
        'premium_amount': monthly_premiums.round(2),
        'premium_frequency': np.random.choice(['Monthly', 'Quarterly', 'Annual'], 
                                            n_customers, p=[0.70, 0.20, 0.10]),
        'payment_method': np.random.choice(['AutoPay', 'Manual'], 
                                         n_customers, p=[0.65, 0.35]),
        'riders': np.random.poisson(0.5, n_customers).clip(0, 3)
    }
    return pd.DataFrame(data)

def generate_transactions(customer_df, policy_df, labels_df):
    """Generate transaction history"""
    transactions = []
    
    for idx, row in policy_df.iterrows():
        customer_id = row['customer_id']
        start_date = row['policy_start_date']
        premium = row['premium_amount']
        frequency = row['premium_frequency']
        payment_method = row['payment_method']
        is_churned = labels_df[labels_df['customer_id'] == customer_id]['churned'].values[0]
        
        # Determine end date (churn date or current date)
        if is_churned:
            churn_date = labels_df[labels_df['customer_id'] == customer_id]['churn_date'].values[0]
            end_date_cust = pd.to_datetime(churn_date)
        else:
            end_date_cust = end_date
        
        # Generate premium payments
        current_date = start_date
        payment_count = 0
        
        while current_date < end_date_cust:
            # Determine next payment date based on frequency
            if frequency == 'Monthly':
                next_date = current_date + timedelta(days=30)
            elif frequency == 'Quarterly':
                next_date = current_date + timedelta(days=90)
            else:  # Annual
                next_date = current_date + timedelta(days=365)
            
            if next_date > end_date_cust:
                break
            
            # Payment behavior (more likely to miss payments if churning)
            if payment_method == 'AutoPay':
                miss_probability = 0.02 if not is_churned else 0.15
            else:
                miss_probability = 0.08 if not is_churned else 0.30
            
            payment_missed = random.random() < miss_probability
            
            # Generate payment record
            if payment_missed:
                days_overdue = random.randint(1, 30)
                payment_date = next_date + timedelta(days=days_overdue)
                status = 'Failed' if random.random() < 0.3 else 'Success'
            else:
                payment_date = next_date
                days_overdue = 0
                status = 'Success'
            
            amount = premium if frequency == 'Monthly' else (premium * 3 if frequency == 'Quarterly' else premium * 12)
            
            transactions.append({
                'customer_id': customer_id,
                'transaction_date': payment_date,
                'transaction_type': 'Premium',
                'amount': amount,
                'payment_status': status,
                'days_overdue': days_overdue
            })
            
            # Add some inquiries
            if random.random() < 0.1:
                inquiry_date = payment_date + timedelta(days=random.randint(1, 20))
                if inquiry_date < end_date_cust:
                    transactions.append({
                        'customer_id': customer_id,
                        'transaction_date': inquiry_date,
                        'transaction_type': 'Inquiry',
                        'amount': 0,
                        'payment_status': 'Success',
                        'days_overdue': 0
                    })
            
            current_date = next_date
            payment_count += 1
    
    return pd.DataFrame(transactions)

def generate_engagement(customer_df, policy_df, labels_df):
    """Generate customer engagement data"""
    engagement = []
    
    for idx, row in customer_df.iterrows():
        customer_id = row['customer_id']
        is_churned = labels_df[labels_df['customer_id'] == customer_id]['churned'].values[0]
        
        # Churned customers tend to have lower engagement
        if is_churned:
            login_freq = np.random.poisson(0.5)
            email_open_rate = np.random.beta(2, 8)  # Lower open rate
            cs_calls = np.random.poisson(2.5)  # More calls (issues)
            complaints = np.random.poisson(0.8)
            mobile_app_prob = 0.2
        else:
            login_freq = np.random.poisson(2)
            email_open_rate = np.random.beta(5, 5)  # Moderate open rate
            cs_calls = np.random.poisson(0.8)
            complaints = np.random.poisson(0.1)
            mobile_app_prob = 0.45
        
        # Convert numpy int64 timestamp to datetime object for date arithmetic
        policy_start = pd.to_datetime(policy_df[policy_df['customer_id'] == customer_id]['policy_start_date'].values[0])
        last_login = generate_date_between(policy_start, end_date)
        
        engagement.append({
            'customer_id': customer_id,
            'last_login_date': last_login,
            'login_frequency_30d': login_freq,
            'mobile_app_user': 'Yes' if random.random() < mobile_app_prob else 'No',
            'email_opens_6m': round(email_open_rate, 2),
            'customer_service_calls_12m': cs_calls,
            'complaints_filed': complaints
        })
    
    return pd.DataFrame(engagement)

def generate_labels(customer_df):
    """Generate churn labels"""
    n_customers = len(customer_df)
    n_churned = int(n_customers * churn_rate)
    
    # Create churn vector
    churn_vector = np.zeros(n_customers)
    churn_indices = np.random.choice(n_customers, n_churned, replace=False)
    churn_vector[churn_indices] = 1
    
    # Generate churn dates and reasons
    churn_dates = []
    churn_reasons = []
    
    for i in range(n_customers):
        if churn_vector[i] == 1:
            # Churn within last 90 days of dataset
            churn_date = generate_date_between(end_date - timedelta(days=90), end_date)
            churn_dates.append(churn_date)
            
            # Churn reasons
            reason = np.random.choice(['Price', 'Service', 'Financial', 'Competition', 'Life_Change', 'Unknown'],
                                    p=[0.25, 0.15, 0.20, 0.15, 0.15, 0.10])
            churn_reasons.append(reason)
        else:
            churn_dates.append(None)
            churn_reasons.append(None)
    
    labels = pd.DataFrame({
        'customer_id': customer_df['customer_id'],
        'churned': churn_vector.astype(int),
        'churn_date': churn_dates,
        'churn_reason': churn_reasons
    })
    
    return labels

# Generate all datasets
print("Generating synthetic life insurance data...")

# Generate base datasets
customer_info = generate_customer_info(n_customers)
print(f"✓ Generated customer_info: {len(customer_info)} records")

labels = generate_labels(customer_info)
print(f"✓ Generated labels: {labels['churned'].sum()} churned customers ({labels['churned'].mean()*100:.1f}%)")

policy_data = generate_policy_data(customer_info)
print(f"✓ Generated policy_data: {len(policy_data)} records")

transactions = generate_transactions(customer_info, policy_data, labels)
print(f"✓ Generated transactions: {len(transactions)} records")

engagement = generate_engagement(customer_info, policy_data, labels)
print(f"✓ Generated engagement: {len(engagement)} records")

# Save datasets
customer_info.to_csv('customer_info.csv', index=False)
policy_data.to_csv('policy_data.csv', index=False)
transactions.to_csv('transactions.csv', index=False)
engagement.to_csv('engagement.csv', index=False)
labels.to_csv('labels.csv', index=False)

print("\nAll datasets saved successfully!")

# Display sample data
print("\nSample data preview:")
print("\nCustomer Info (first 5 rows):")
print(customer_info.head())

print("\nPolicy Data (first 5 rows):")
print(policy_data.head())

print("\nTransactions (first 10 rows):")
print(transactions.head(10))

print("\nEngagement (first 5 rows):")
print(engagement.head())

print("\nLabels (churned customers):")
print(labels[labels['churned'] == 1].head())

# Basic statistics
print("\n" + "="*50)
print("DATASET STATISTICS")
print("="*50)

print("\nChurn Statistics:")
print(f"- Total customers: {n_customers}")
print(f"- Churned customers: {labels['churned'].sum()}")
print(f"- Churn rate: {labels['churned'].mean()*100:.1f}%")

print("\nPolicy Distribution:")
print(policy_data['policy_type'].value_counts())

print("\nPayment Method Distribution:")
print(policy_data['payment_method'].value_counts())

print("\nTransaction Summary:")
print(f"- Total transactions: {len(transactions)}")
print(f"- Failed payments: {(transactions['payment_status'] == 'Failed').sum()}")
print(f"- Average days overdue: {transactions['days_overdue'].mean():.2f}")

print("\nEngagement Summary:")
print(f"- Mobile app users: {(engagement['mobile_app_user'] == 'Yes').sum()} ({(engagement['mobile_app_user'] == 'Yes').mean()*100:.1f}%)")
print(f"- Avg email open rate: {engagement['email_opens_6m'].mean()*100:.1f}%")
print(f"- Avg CS calls per customer: {engagement['customer_service_calls_12m'].mean():.2f}")