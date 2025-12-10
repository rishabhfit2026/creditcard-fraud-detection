import streamlit as st
import joblib
import numpy as np

# Load model & scaler
model = joblib.load("optuna_xgb_fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💳 Credit Card Fraud Detection App")
st.write("Enter transaction details to predict whether it's fraud or not.")

# User input section
def user_input():
    st.subheader("Enter 30 Features (Time, V1...V28, Amount)")
    feature_values = []

    feature_names = [
        "Time"
    ] + [f"V{i}" for i in range(1, 29)] + ["Amount"]

    for name in feature_names:
        value = st.number_input(name, value=0.0, format="%.6f")
        feature_values.append(value)

    return np.array(feature_values).reshape(1, -1)

# Get input from UI
input_data = user_input()

# Predict
if st.button("Predict Fraud"):
    scaled = scaler.transform(input_data)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    st.subheader("🔍 Prediction Result")

    if pred == 1:
        st.error(f"⚠️ FRAUD DETECTED! (Probability = {prob:.4f})")
    else:
        st.success(f"✅ NOT Fraud (Probability = {prob:.4f})")
