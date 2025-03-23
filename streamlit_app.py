import streamlit as st
import requests

# Define the FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000/recommend"

# Streamlit app title
st.title("Insurance Product Recommendation System")

# Input form for customer data
st.header("Enter Customer Details")
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
account_type = st.selectbox("Account Type", ["Current", "Savings"])
account_balance = st.number_input("Account Balance", min_value=0.0, value=5000.0)
loan_type = st.selectbox("Loan Type", ["Auto", "Mortgage", "Personal"])
loan_status = st.selectbox("Loan Status", ["Approved", "Rejected", "Closed"])
credit_limit = st.number_input("Credit Limit", min_value=0.0, value=3000.0)
credit_card_balance = st.number_input("Credit Card Balance", min_value=0.0, value=1000.0)
anomaly = st.selectbox("Anomaly", [0, 1])

# Button to trigger the recommendation
if st.button("Get Recommendation"):
    # Prepare the input data
    input_data = {
        "Age": age,
        "Gender": gender,
        "Account_Type": account_type,
        "Account_Balance": account_balance,
        "Loan_Type": loan_type,
        "Loan_Status": loan_status,
        "Credit_Limit": credit_limit,
        "Credit_Card_Balance": credit_card_balance,
        "Anomaly": anomaly
    }

    # Send a POST request to the FastAPI backend
    response = requests.post(FASTAPI_URL, json=input_data)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        recommended_product = result.get("recommended_product", "No recommendation")
        explanation = result.get("explanation", "No explanation available")

        # Display the recommendation and explanation
        st.success(f"Recommended Product: **{recommended_product}**")
        st.info(f"Explanation: {explanation}")
    else:
        st.error("Failed to get a recommendation. Please check the input data and try again.")