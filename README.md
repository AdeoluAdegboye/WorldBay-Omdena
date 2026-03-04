 WorldBay Credit Scoring System
A machine learning-powered alternative credit scoring application built for WorldBay Technologies (Grocedy), developed as part of an Omdena collaborative AI project. The system generates Customer Lifetime Value (CLV) scores for underbanked Nigerian users — enabling access to micro-financial services using behavioural payment data rather than traditional credit history.

🌍 Background & Problem Statement
WorldBay offers a food subscription service where customers pay for grocery parcels in instalments over 27 days before receiving their package. The majority of users are unbanked with no formal financial footprint, making them ineligible for traditional credit products.
WorldBay partnered with Omdena to build an alternative credit scoring model using customers' in-app payment behaviour. The resulting scores are designed to unlock:

🏦 Micro-loans
🛡️ Micro-insurance
💰 Micro-pensions
📦 Upgraded subscription plans


🏗️ Architecture
[WorldBay Transaction Data]
         │
         ▼
[Feature Engineering]          49 features engineered from raw transaction logs
         │
         ▼
[Random Forest Regressor]      Trained model serialised to Final_Final.pkl
         │
         ▼
[SHAP Analysis]                Feature importance and prediction explainability
         │
         ▼
[Streamlit Web App]            Login-gated UI for score prediction & data insights

📁 Project Structure
WorldBay-Omdena/
├── WBOmdena.py             # Main Streamlit application
├── Final_Final.pkl         # Trained Random Forest model (serialised)
├── requirements.txt        # Python dependencies
├── README.md
└── assets/                 # Dashboard images and visualisations
    ├── worldbay logo.jpg
    ├── grocedy.jpg
    ├── modelsummary.png
    ├── EDA bar plot.png
    ├── MagMonthly.png
    ├── branches.png
    ├── Agentsoverview.png
    └── amounts.png

⚙️ Tech Stack
ToolPurposePython / Pandas / NumPyData processing and feature engineeringScikit-learnRandom Forest model training and predictionSHAPModel explainability and feature importanceStreamlitInteractive web applicationSQLiteLocal user authentication databasePickleModel serialisationMatplotlibData visualisations

🤖 Model & Features
Feature Engineering
A total of 49 features were engineered from raw transaction data, grouped into four categories:
CategoryCountExamplesTransaction behaviour43Frequency, recency, monetary value, days past dueRepayment behaviour2Probability of purchase in 30 days, active plan probabilityDemographics2Age in days, incomeDateTime4Payment terms, subscription period active
Top 5 Predictors (by SHAP importance)

prob_of_predicted_purchases_30d — Predicted purchase probability over next 30 days
monetary_value — Value of the customer's requested loan/plan
prob_is_active_30d — Probability of having an active plan in 30 days
4.91 - 180 days — Activity window feature
cond_expected_avg_profit — Expected average profit contribution

Model Performance
Adding more than 10 engineered features improved model accuracy from 50% → 85%.
Algorithm

Random Forest Regressor — selected for robustness to missing data and non-linear feature interactions
SHAP analysis used post-training to explain individual predictions using Shapley values (Lundberg & Lee, 2017)


🚀 Getting Started
Prerequisites

Python 3.8+
The trained model file Final_Final.pkl (not included in repo — contact for access)

Installation
bashgit clone https://github.com/AdeoluAdegboye/WorldBay-Omdena.git
cd WorldBay-Omdena
pip install -r requirements.txt
Run the App
bashstreamlit run WBOmdena.py
The app will open at http://localhost:8501.

🖥️ Application Features
The Streamlit app is login-gated with three main sections:
Home — Landing page with WorldBay branding
Predict Credit Score — Form-based input for 36 customer features; outputs a CLV score and displays a SHAP model summary chart. Input features include:

Transaction behaviour (invoices, frequency, recency, monetary value)
Subscription status and plan tier
Payment terms and days past due date
Probability scores for future activity

Data Insights — EDA visualisations including:

Pick-up and delivery task distribution (2019–2022)
Monthly trip spread
Top branch locations
Agent performance overview
Transaction amount distribution


📊 Key Findings

~7,927 customers identified as repeat customers with at least two transactions
Features like gender and implied marital status were dropped due to high null rates
The model significantly benefits from behavioural features over demographic ones, supporting a privacy-respecting, behaviour-first scoring approach


💡 Potential Improvements

Replace pickle with MLflow for proper model versioning and experiment tracking
Add SHAP waterfall plots per prediction so users can see exactly why a score was generated
Improve the input form UX — group the 36 fields into logical sections and add tooltips explaining each feature in plain language
Replace SQLite auth with a proper auth provider (e.g. Firebase Auth or Auth0) for production use
Add score banding — translate the raw CLV output into labelled tiers (e.g. Bronze / Silver / Gold) for easier interpretation
Collect additional features — income level, employment status, marital status — to further improve model accuracy as suggested by the analysis


🤝 Built With
This project was developed collaboratively as part of an Omdena challenge — a global platform for AI engineers to solve real-world problems through collaborative projects.

📬 Contact
Adeolu Adegboye · GitHub
