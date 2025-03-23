import pandas as pd
import numpy as np
from models.model_loader import load_model
from src.utils.explanation import generate_explanation

def recommend_product(customer_data):
    model, pca, scaler = load_model()

    # Convert to DataFrame
    customer_df = pd.DataFrame([customer_data])

    # Rename columns to match training feature names
    column_mapping = {
        "Account_Balance": "Account Balance",
        "Credit_Card_Balance": "Credit Card Balance",
        "Credit_Limit": "Credit Limit",
        "Account_Type": "Account Type",
        "Loan_Status": "Loan Status",
    }
    customer_df.rename(columns=column_mapping, inplace=True)

    # Apply one-hot encoding for categorical variables
    customer_df = pd.get_dummies(customer_df, columns=['Gender', 'Account Type', 'Loan Status'], drop_first=True)

    # Define expected feature names (must match training)
    expected_columns = [
        'Age', 'Account Balance', 'Credit Limit', 'Credit Card Balance', 'Anomaly',
        'Gender_Male', 'Gender_Other', 'Account Type_Savings', 'Loan Status_Closed', 'Loan Status_Rejected'
    ]

    # Add missing columns with default value 0
    for col in expected_columns:
        if col not in customer_df.columns:
            customer_df[col] = 0

    # Reorder columns to match training
    customer_df = customer_df[expected_columns]

    # Standardize the data using the trained scaler
    customer_scaled = scaler.transform(customer_df)

    # Apply PCA transformation
    customer_pca = pca.transform(customer_scaled)

    # Predict the product
    prediction = model.predict(customer_pca)

    # Take only the first prediction if multiple are returned
    # and convert from numpy type to regular Python string
    if prediction.size > 0:
        recommended_product = prediction[0]
        # If it's still an array, take the first element
        if hasattr(recommended_product, 'size') and recommended_product.size > 0:
            recommended_product = recommended_product[0]
        recommended_product = str(recommended_product)
    else:
        recommended_product = "No recommendation"

    # Generate explanation using Gemini
    explanation = generate_explanation(customer_data, recommended_product)

    return {
        "recommended_product": recommended_product,
        "explanation": explanation
    }
