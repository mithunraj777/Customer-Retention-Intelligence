from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load artifacts
model = joblib.load(
    r"D:\Projects\Customer Churn Prediction\models\churn_model.pkl"
)

scaler = joblib.load(
    r"D:\Projects\Customer Churn Prediction\models\scaler.pkl"
)

feature_names = joblib.load(
    r"D:\Projects\Customer Churn Prediction\models\feature_names.pkl"
)

numeric_features = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # ----------------------------
    # Numeric Inputs
    # ----------------------------

    tenure = float(request.form["tenure"])
    monthly = float(request.form["monthly"])
    total = float(request.form["total"])

    # ----------------------------
    # Categorical Inputs
    # ----------------------------

    gender = request.form["gender"]
    senior = int(request.form["senior"])
    partner = request.form["partner"]
    dependents = request.form["dependents"]

    phone = request.form["phone"]
    multiline = request.form["multiline"]

    internet = request.form["internet"]

    security = request.form["security"]
    backup = request.form["backup"]
    protection = request.form["protection"]
    tech = request.form["tech"]

    tv = request.form["tv"]
    movies = request.form["movies"]

    contract = request.form["contract"]

    paperless = request.form["paperless"]

    payment = request.form["payment"]

    # ----------------------------
    # Create Empty Feature Vector
    # ----------------------------

    row = pd.DataFrame(
        [[0] * len(feature_names)],
        columns=feature_names
    )

    # ----------------------------
    # Numerical Features
    # ----------------------------

    row["SeniorCitizen"] = senior
    row["tenure"] = tenure
    row["MonthlyCharges"] = monthly
    row["TotalCharges"] = total

    # ----------------------------
    # Binary Features
    # ----------------------------

    if gender == "Male":
        row["gender_Male"] = 1

    if partner == "Yes":
        row["Partner_Yes"] = 1

    if dependents == "Yes":
        row["Dependents_Yes"] = 1

    if phone == "Yes":
        row["PhoneService_Yes"] = 1

    # ----------------------------
    # Multiple Lines
    # ----------------------------

    if multiline == "Yes":
        row["MultipleLines_Yes"] = 1

    elif multiline == "No phone service":
        row["MultipleLines_No phone service"] = 1

    # ----------------------------
    # Internet Service
    # ----------------------------

    if internet == "Fiber optic":
        row["InternetService_Fiber optic"] = 1

    elif internet == "No":
        row["InternetService_No"] = 1

    # ----------------------------
    # Online Security
    # ----------------------------

    if security == "Yes":
        row["OnlineSecurity_Yes"] = 1

    elif security == "No internet service":
        row["OnlineSecurity_No internet service"] = 1

    # ----------------------------
    # Online Backup
    # ----------------------------

    if backup == "Yes":
        row["OnlineBackup_Yes"] = 1

    elif backup == "No internet service":
        row["OnlineBackup_No internet service"] = 1

    # ----------------------------
    # Device Protection
    # ----------------------------

    if protection == "Yes":
        row["DeviceProtection_Yes"] = 1

    elif protection == "No internet service":
        row["DeviceProtection_No internet service"] = 1

    # ----------------------------
    # Tech Support
    # ----------------------------

    if tech == "Yes":
        row["TechSupport_Yes"] = 1

    elif tech == "No internet service":
        row["TechSupport_No internet service"] = 1

    # ----------------------------
    # Streaming TV
    # ----------------------------

    if tv == "Yes":
        row["StreamingTV_Yes"] = 1

    elif tv == "No internet service":
        row["StreamingTV_No internet service"] = 1

    # ----------------------------
    # Streaming Movies
    # ----------------------------

    if movies == "Yes":
        row["StreamingMovies_Yes"] = 1

    elif movies == "No internet service":
        row["StreamingMovies_No internet service"] = 1

    # ----------------------------
    # Contract
    # ----------------------------

    if contract == "One year":
        row["Contract_One year"] = 1

    elif contract == "Two year":
        row["Contract_Two year"] = 1

    # ----------------------------
    # Paperless Billing
    # ----------------------------

    if paperless == "Yes":
        row["PaperlessBilling_Yes"] = 1

    # ----------------------------
    # Payment Method
    # ----------------------------

    if payment == "Credit card (automatic)":
        row["PaymentMethod_Credit card (automatic)"] = 1

    elif payment == "Electronic check":
        row["PaymentMethod_Electronic check"] = 1

    elif payment == "Mailed check":
        row["PaymentMethod_Mailed check"] = 1

    # ----------------------------
    # Scaling
    # ----------------------------

    row[numeric_features] = scaler.transform(
        row[numeric_features]
    )

    # ----------------------------
    # Prediction
    # ----------------------------

    probability = model.predict_proba(row)[0][1]

    if probability >= 0.70:
        risk = "HIGH"
        recommendation = (
            "Offer retention discount, annual contract upgrade, "
            "and premium customer support."
        )

    elif probability >= 0.40:
        risk = "MEDIUM"
        recommendation = (
            "Increase engagement through personalized offers."
        )

    else:
        risk = "LOW"
        recommendation = (
            "Customer appears stable."
        )

    return render_template(
        "index.html",
        probability=round(probability * 100, 2),
        risk=risk,
        recommendation=recommendation
    )


if __name__ == "__main__":
    app.run(debug=True)