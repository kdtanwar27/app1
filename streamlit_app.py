import streamlit as st
import requests

st.title("💸 Loan Risk Prediction")
st.write("Enter the loan application details:")

income = st.number_input("Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
credit_score = st.slider("Credit Score", min_value=300, max_value=850)

if st.button("Predict Risk"):
    payload = {
        "income": income,
        "loan_amount": loan_amount,
        "credit_score": credit_score
    }

    response = requests.post("http://127.0.0.1:8000/api/predict/", json=payload)

    if response.status_code == 200:
        st.success(f"Prediction: {response.json()['risk']}")
    else:
        st.error("Error: Could not fetch prediction.")