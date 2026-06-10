# Customer Churn Prediction System

## Overview

This project is an end-to-end Machine Learning application that predicts customer churn using the IBM Telco Customer Churn Dataset.

The goal is to identify customers who are likely to leave a telecom service provider and provide actionable retention recommendations.

---

## Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Hyperparameter Tuning
- SHAP Explainability
- Model Comparison
- Flask Web Application
- Churn Risk Prediction
- Retention Recommendations

---

## Dataset

IBM Telco Customer Churn Dataset

### Target Variable

- Churn
  - Yes → Customer leaves
  - No → Customer stays

### Dataset Size

- 7043 Customers
- 21 Original Features

---

## Machine Learning Workflow

1. Data Cleaning
2. Missing Value Handling
3. Feature Encoding
4. Feature Scaling
5. Train-Test Split
6. Model Training
7. Hyperparameter Tuning
8. Model Evaluation
9. Explainable AI using SHAP
10. Deployment using Flask

---

## Models Used

### Logistic Regression

- Simple and interpretable baseline model

### Decision Tree

- Rule-based classification model

### Random Forest

- Ensemble learning method

### XGBoost

- Gradient boosting algorithm used for high-performance prediction

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Example Results:

| Model | Accuracy | ROC-AUC |
|---------|---------|---------|
| Logistic Regression | 80.6% | 0.842 |
| Decision Tree | 79.4% | 0.827 |
| Random Forest | 79.0% | 0.826 |

---

## Explainable AI

SHAP (SHapley Additive exPlanations) was used to:

- Interpret model predictions
- Identify key churn drivers
- Improve model transparency

---

## Web Application

The Flask application allows users to:

- Enter customer information
- Predict churn probability
- View risk level
- Receive retention recommendations

---

## Project Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl
│
├── reports/
│   └── shap_summary.png
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Customer-Churn-Prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

- Streamlit Dashboard
- Customer Segmentation
- Docker Deployment
- Cloud Deployment
- Automated Retraining Pipeline

---

## Author

**Mithunraj T**

B.Tech Artificial Intelligence & Machine Learning

Machine Learning | Data Science | AI Enthusiast