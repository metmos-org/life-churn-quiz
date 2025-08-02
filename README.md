# Life Insurance Customer Retention Case Study

## Context
SecureLife Insurance is experiencing a 15% annual customer churn rate. You've been tasked with building a predictive model to identify at-risk customers and provide actionable retention strategies.

## Your Goal
Build a machine learning model to predict which customers will cancel their life insurance policy in the next 90 days.

## Getting Started

### 1. Environment Setup

Follow the complete setup instructions in [CLAUDE.md](CLAUDE.md) to install:
- pyenv (Python version manager)
- Python 3.13
- pipx (Python application installer)
- Poetry (dependency manager)

### 2. Install Dependencies
```bash
poetry install
poetry shell
```

### 3. Generate Sample Data
```bash
python generate_insurance_data.py
```

This creates 5 CSV files with synthetic insurance data:
- `customer_info.csv` - Demographics (age, income, marital status, etc.)
- `policy_data.csv` - Policy details (type, amount, premiums)
- `transactions.csv` - Payment history and transaction records
- `engagement.csv` - Customer interaction metrics
- `labels.csv` - **Target variable** (churned/active customers)

## Data Description

### Dataset Structure
- **10,000 customers** with realistic demographic distributions
- **15% churn rate** (1,500 churned customers)
- **Time series data** spanning 2022-2024
- **Multiple data sources** simulating real insurance systems

### Key Features for ML Modeling

**Customer Demographics:**
- Age, gender, marital status, dependents
- Income bracket, employment status, education level

**Policy Information:**
- Policy type (Term/Whole/Universal), coverage amount
- Premium amounts and payment frequency
- Additional riders

**Payment Behavior:**
- Transaction history with payment status
- Days overdue, payment method preferences
- Failed payment patterns

**Engagement Metrics:**
- Login frequency, mobile app usage
- Email open rates, customer service calls
- Complaint history

### Target Variable
- `churned`: Binary (0=Active, 1=Churned)
- `churn_date`: When customer churned
- `churn_reason`: Why they churned (Price, Service, etc.)

## Tasks

### 1. Exploratory Data Analysis
- Merge datasets and check data quality
- Visualize churn patterns across customer segments
- Identify key insights for feature engineering

### 2. Feature Engineering
Create meaningful features such as:
- Policy tenure
- Payment behavior metrics
- Customer engagement scores
- Any other relevant features

### 3. Model Development
- Split data (60/20/20 for train/validation/test)
- Train at least 3 different models
- Evaluate performance (focus on AUC-ROC)
- Identify important features

### 4. Business Recommendations
- Top 5 churn drivers
- 3 targeted retention strategies
- Implementation considerations

## Extending the Template

### Customize Data Generation
Modify parameters in `generate_insurance_data.py`:
```python
n_customers = 10000      # Number of customers
churn_rate = 0.15        # Percentage who churn
start_date = datetime(2022, 1, 1)  # Data period
end_date = datetime(2024, 1, 1)
```

### Add New Features
- Modify data generation functions to include additional customer attributes
- Add new behavioral patterns or external factors
- Incorporate seasonal trends or economic indicators

### Advanced Scenarios
- **Multi-product customers**: Extend to customers with multiple policies
- **Time-to-churn prediction**: Predict when customers will churn
- **Retention intervention**: Simulate the effect of retention campaigns

## Deliverables
1. Completed Jupyter notebook with code and analysis
2. Brief summary of findings and recommendations

## Evaluation Criteria
- Code quality and ML best practices
- Feature engineering creativity
- Model performance (target AUC-ROC > 0.75)
- Business insight quality
- Clear communication

## Tips for Success

- **Join tables intelligently**: Customer behavior emerges from combining datasets
- **Time matters**: Recent behavior is more predictive than historical patterns
- **Feature interactions**: Combine demographic and behavioral features
- **Validation strategy**: Use time-based splits to avoid data leakage
- **Interpretability**: Focus on explainable models for business stakeholders

## Project Structure Suggestions

```
├── data/                   # Generated CSV files
├── notebooks/             # Jupyter notebooks for EDA
├── src/                   # Source code modules
│   ├── data_processing.py # Data loading and cleaning
│   ├── feature_engineering.py
│   ├── modeling.py        # ML model training
│   └── evaluation.py      # Model evaluation
├── models/                # Saved model artifacts
├── reports/               # Analysis reports and visualizations
└── tests/                 # Unit tests (bonus points!)
```

Good luck with your machine learning challenge! 🚀

---

**Note:** This is synthetic data for educational purposes. Real insurance data would require additional privacy and regulatory considerations.