# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a life insurance customer retention case study project called "life-churn". It generates synthetic life insurance datasets for churn analysis and machine learning modeling.

## Development Commands

### Initial Setup (First Time Only)

1. **Install pyenv** - Python version manager for managing multiple Python versions
```bash
# macOS with Homebrew
brew install pyenv

# Add to shell profile (~/.zshrc or ~/.bash_profile)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

2. **Install Python 3.13** using pyenv
```bash
pyenv install 3.13.0
pyenv global 3.13.0
```

3. **Install pipx** - Tool for installing Python applications in isolated environments
```bash
# macOS with Homebrew
brew install pipx

# Or using pip
python -m pip install --user pipx
python -m pipx ensurepath
```

4. **Install Poetry** - Dependency management and packaging tool for Python projects
```bash
pipx install poetry
```

### Environment Setup
```bash
# Install dependencies using Poetry
poetry install

# Activate virtual environment
poetry shell
```

### Data Generation
```bash
# Generate synthetic insurance datasets
python generate_insurance_data.py
```

This will create 5 CSV files:
- `customer_info.csv` - Customer demographics and personal info
- `policy_data.csv` - Insurance policy details and premiums
- `transactions.csv` - Payment history and transaction records
- `engagement.csv` - Customer engagement metrics
- `labels.csv` - Churn labels and reasons

### Python Environment
- Requires Python >=3.13
- Uses Poetry for dependency management
- Key dependencies: pandas, numpy, matplotlib, seaborn

## Data Architecture

The project follows a multi-table relational structure centered around customer churn prediction:

### Core Data Flow
1. **Customer Demographics** (`customer_info.csv`) - Base customer attributes (age, income, marital status, etc.)
2. **Policy Information** (`policy_data.csv`) - Insurance products, coverage amounts, premium calculations
3. **Transaction History** (`transactions.csv`) - Payment records, overdue payments, inquiries
4. **Engagement Metrics** (`engagement.csv`) - Digital interaction patterns, service calls, complaints
5. **Churn Labels** (`labels.csv`) - Target variable with churn dates and reasons

### Key Relationships
- All tables link via `customer_id` (format: `CUST_######`)
- Policy amounts are influenced by customer income brackets
- Premium calculations factor in age and coverage amount
- Transaction patterns differ between churned and active customers
- Engagement metrics correlate with churn propensity

### Data Generation Logic
- Uses fixed random seeds (42) for reproducibility
- 10,000 customers with 15% churn rate by default
- Realistic distributions for demographics and policy types
- Time-based transaction generation with payment behavior modeling
- Churned customers show distinct patterns (more missed payments, lower engagement)

## Configuration

All key parameters are defined at the top of `generate_insurance_data.py`:
- `n_customers`: Number of customers to generate (default: 10,000)
- `churn_rate`: Percentage of customers who churn (default: 0.15)
- `start_date` / `end_date`: Data collection time period (2022-2024)