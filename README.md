# Life Insurance Customer Churn Prediction - ML Quiz Template

This is a machine learning quiz template for building a customer churn prediction model using synthetic life insurance data. The project generates realistic datasets that simulate real-world insurance customer behavior patterns.

## Quiz Overview

**Objective:** Build a machine learning model to predict which life insurance customers are likely to churn (cancel their policies).

**Your Task:** Use the provided data generation template to create training data, then develop and evaluate ML models for churn prediction.

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

## ML Challenge Tasks

### Task 1: Exploratory Data Analysis
- Load and explore the generated datasets
- Analyze churn patterns across different customer segments
- Identify key features that correlate with churn

### Task 2: Feature Engineering
- Create meaningful features from the multi-table structure
- Handle time-series aspects of transaction data
- Engineer features that capture customer behavior changes

### Task 3: Model Development
- Build classification models to predict churn
- Try different algorithms (Logistic Regression, Random Forest, XGBoost, etc.)
- Handle class imbalance (15% churn rate)

### Task 4: Model Evaluation
- Use appropriate metrics for imbalanced classification
- Implement proper train/validation/test splits
- Evaluate model performance and feature importance

### Task 5: Business Impact Analysis
- Calculate potential revenue saved by preventing churn
- Develop retention strategies based on model insights
- Create actionable recommendations for the insurance company

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

## Success Criteria

Your solution should demonstrate:
1. **Data Understanding**: Clear analysis of customer patterns and churn drivers
2. **Feature Engineering**: Creative use of multi-table data structure
3. **Model Performance**: Achieve meaningful predictive accuracy
4. **Business Value**: Translate ML results into actionable business insights
5. **Code Quality**: Clean, well-documented, reproducible code

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