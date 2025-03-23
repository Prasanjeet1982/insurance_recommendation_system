import joblib

def load_model():
    """Load trained model, PCA, and scaler."""
    model = joblib.load("models/model.pkl")
    pca = joblib.load("models/pca.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, pca, scaler