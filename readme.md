# **Insurance Recommendation System**

## 📌 Overview
The **Insurance Recommendation System** is a FastAPI-based machine learning application that recommends insurance products based on customer data. It also provides AI-generated explanations using Google Gemini AI. The system includes:
- **FastAPI Backend** for API services.
- **Streamlit Frontend** for an interactive UI.
- **Machine Learning Model** (Random Forest, PCA, Scaler) for predictions.
- **Docker & Docker Compose** for containerized deployment.

---

## 🚀 **Getting Started**

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- **Python 3.9+**
- **Docker & Docker Compose**
- **Google Gemini API Key** (for explanations)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/insurance-recommendation.git
cd insurance-recommendation
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory:
```sh
touch .env
```
Edit the `.env` file and add your Google API key:
```sh
GOOGLE_API_KEY=your_actual_api_key_here
```

> ⚠ **Ensure `.env` is added to `.gitignore`** to keep credentials safe!

---

## 🐳 **Running with Docker Compose**

### **1️⃣ Build & Start Containers**
```sh
docker-compose up --build
```
This will:
- Start **FastAPI backend** at `http://localhost:8000`
- Start **Streamlit frontend** at `http://localhost:8501`

### **2️⃣ Verify Running Containers**
```sh
docker ps
```

### **3️⃣ Stop Containers**
```sh
docker-compose down
```

---

## 🎯 **Using the System**

### **FastAPI Endpoints**
- **Swagger API Docs:** [`http://localhost:8000/docs`](http://localhost:8000/docs)
- **Recommend Insurance Product:**
  ```sh
  curl -X POST "http://localhost:8000/recommend" -H "Content-Type: application/json" -d '{
      "Age": 30,
      "Gender": "Male",
      "Account_Type": "Savings",
      "Account_Balance": 5000,
      "Loan_Type": "Personal",
      "Loan_Status": "Approved",
      "Credit_Limit": 3000,
      "Credit_Card_Balance": 1000,
      "Anomaly": 0
  }'
  ```

### **Streamlit UI**
1. Open a browser and visit: [`http://localhost:8501`](http://localhost:8501)
2. Enter customer details and get a recommendation.

---

## 🔧 **Development Setup (Without Docker)**

### ** 1 Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### ** 2 Install Dependencies**
```sh
pip install -r requirements.txt
```
### ** 3 Run FastAPI Backend**
```sh
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### ** 4 Run FastAPI Backend**
```sh
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### ** 5 Run Streamlit Frontend**
```sh
streamlit run streamlit_app.py
```

---

## 📊 **System Architecture**
- **FastAPI Backend** → Handles API requests.
- **ML Model (Random Forest)** → Predicts insurance recommendations.
- **Google Gemini AI** → Generates explanation texts.
- **Docker & Compose** → Manages containerized deployment.

![Architecture Diagram](architecture.png) *(Replace with your actual diagram)*

---

## 🛠 **Future Improvements**
- ✅ **Database Integration (PostgreSQL)** for storing customer recommendations.
- ✅ **Improve ML Model** with XGBoost and fine-tuning.
- ✅ **Enhance AI Explanation** by fine-tuning Gemini AI.
- ✅ **Add CI/CD Pipeline** for automatic deployment.

---

## 📝 **License**
This project is licensed under the MIT License.

---

## 🤝 **Contributing**
We welcome contributions! Feel free to fork the repository and submit a PR.

### **Author:**
🚀 **Your Name** - [GitHub](https://github.com/your-profile)

