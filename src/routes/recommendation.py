from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.recommendation_service import recommend_product

router = APIRouter()

class CustomerData(BaseModel):
    Age: int
    Gender: str
    Account_Type: str
    Account_Balance: float
    Loan_Type: str
    Loan_Status: str
    Credit_Limit: float
    Credit_Card_Balance: float
    Anomaly: int

@router.post("/recommend")
def recommend(customer_data: CustomerData):
    return recommend_product(customer_data.dict())