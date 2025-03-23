import google.generativeai as genai
from src.config.settings import GOOGLE_API_KEY

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

def generate_explanation(customer_data, recommended_product):
    """Generate an explanation for the recommended product using Gemini."""
    prompt = f"""
    You are an insurance expert providing personalized product recommendations to customers. Your task is to explain why a specific insurance product is recommended for a customer based on their profile.

    **Customer Profile:**
    - Age: {customer_data['Age']}
    - Gender: {customer_data['Gender']}
    - Account Type: {customer_data['Account_Type']}
    - Account Balance: {customer_data['Account_Balance']}
    - Loan Type: {customer_data['Loan_Type']}
    - Loan Status: {customer_data['Loan_Status']}
    - Credit Limit: {customer_data['Credit_Limit']}
    - Credit Card Balance: {customer_data['Credit_Card_Balance']}
    - Anomaly: {customer_data['Anomaly']}

    **Recommended Product:** {recommended_product}

    **Task:**
    Explain why this product is recommended for the customer. Consider the following:
    1. How does the customer's profile (age, gender, account type, etc.) align with the recommended product?
    2. What specific features of the product make it suitable for the customer?
    3. How does the product address the customer's financial needs or risks?
    4. Provide a concise and customer-friendly explanation.

    **Example Explanation:**
    "Based on your profile, we recommend the Auto Insurance policy. This policy is ideal for customers with a moderate credit card balance and an active auto loan. It provides comprehensive coverage for your vehicle, ensuring financial protection in case of accidents or damages. Additionally, the policy offers flexible payment options tailored to your account balance and credit limit."

    **Your Explanation:**
    """
    
    # Initialize the Gemini model
    model = genai.GenerativeModel("models/gemini-1.5-pro-001")
    
    # Generate the explanation
    response = model.generate_content(prompt)
    return response.text