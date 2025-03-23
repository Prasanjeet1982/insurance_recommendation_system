import requests

# Define the base URL of the FastAPI server
BASE_URL = "http://127.0.0.1:8000/"

# Test case 1: Valid input
def test_valid_input():
    print("Running test_valid_input...")
    data = {
        "Age": 45,
        "Gender": "Male",
        "Account_Type": "Current",
        "Account_Balance": 1313.38,
        "Loan_Type": "Mortgage",
        "Loan_Status": "Rejected",
        "Credit_Limit": 1737.88,
        "Credit_Card_Balance": 4524.32,
        "Anomaly": -1
    }
    response = requests.post(f"{BASE_URL}/recommend", json=data)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert "recommended_product" in response.json(), "Response does not contain 'recommended_product'"
    print("Test passed! Response:", response.json())

# Test case 2: Missing required field
def test_missing_field():
    print("Running test_missing_field...")
    data = {
        "Age": 45,
        "Gender": "Male",
        "Account_Type": "Current",
        "Account_Balance": 1313.38,
        "Loan_Type": "Mortgage",
        "Loan_Status": "Rejected",
        "Credit_Limit": 1737.88,
        # Missing "Credit_Card_Balance" and "Anomaly"
    }
    response = requests.post(f"{BASE_URL}/recommend", json=data)
    assert response.status_code == 422, f"Expected status code 422, got {response.status_code}"
    print("Test passed! Response:", response.json())

# Test case 3: Invalid data type
def test_invalid_data_type():
    print("Running test_invalid_data_type...")
    data = {
        "Age": "Forty-five",  # Invalid type (should be int)
        "Gender": "Male",
        "Account_Type": "Current",
        "Account_Balance": 1313.38,
        "Loan_Type": "Mortgage",
        "Loan_Status": "Rejected",
        "Credit_Limit": 1737.88,
        "Credit_Card_Balance": 4524.32,
        "Anomaly": 1
    }
    response = requests.post(f"{BASE_URL}/recommend", json=data)
    assert response.status_code == 422, f"Expected status code 422, got {response.status_code}"
    print("Test passed! Response:", response.json())

# Test case 4: Edge case - No recommendation
def test_no_recommendation():
    print("Running test_no_recommendation...")
    data = {
        "Age": 45,
        "Gender": "Male",
        "Account_Type": "Current",
        "Account_Balance": 1313.38,
        "Loan_Type": "Mortgage",
        "Loan_Status": "Rejected",
        "Credit_Limit": 1737.88,
        "Credit_Card_Balance": 4524.32,
        "Anomaly": 1
    }
    response = requests.post(f"{BASE_URL}/recommend", json=data)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert "recommended_product" in response.json(), "Response does not contain 'recommended_product'"
    assert response.json()["recommended_product"] != "No recommendation", "Expected a valid recommendation"
    print("Test passed! Response:", response.json())

# Run all test cases
if __name__ == "__main__":
    test_valid_input()
    test_missing_field()
    test_invalid_data_type()
    test_no_recommendation()