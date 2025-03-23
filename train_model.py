import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import joblib

def load_data(filepath):
    """Load the dataset from a CSV file."""
    data = pd.read_csv(filepath)
    return data

def preprocess_data(data):
    """Preprocess the data for training."""
    # Define features and target
    features = [
        'Age', 'Gender', 'Account Type', 'Account Balance', 'Loan Type', 
        'Loan Status', 'Credit Limit', 'Credit Card Balance', 'Anomaly'
    ]
    target = 'Loan Type'

    # Filter the dataset
    data = data[features + [target]]

    # Handle missing values (if any)
    data = data.dropna()

    # Encode categorical variables
    data = pd.get_dummies(data, columns=['Gender', 'Account Type', 'Loan Status'], drop_first=True)

    # Split the data into training and testing sets
    X = data.drop(columns=[target])
    y = data[target]

    # Ensure y is a 1D array
    if isinstance(y.iloc[0], list):
        y = y.explode()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def apply_pca(X_train, X_test, n_components=5):
    """Apply PCA to reduce dimensionality."""
    # Standardize the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Apply PCA
    pca = PCA(n_components=n_components)
    X_train_pca = pca.fit_transform(X_train_scaled)
    X_test_pca = pca.transform(X_test_scaled)

    return X_train_pca, X_test_pca, pca, scaler

def build_model(X_train, y_train):
    """Build and train the recommendation model."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model's performance."""
    # Make predictions
    y_pred = model.predict(X_test)

    # Convert y_test and y_pred to NumPy arrays
    y_test = y_test.to_numpy()  # Convert DataFrame to NumPy array
    y_pred = y_pred.to_numpy() if hasattr(y_pred, 'to_numpy') else y_pred  # Convert if y_pred is a DataFrame

    # Flatten y_test and y_pred if they are 2D arrays
    if y_test.ndim > 1:
        y_test = y_test.ravel()
    if y_pred.ndim > 1:
        y_pred = y_pred.ravel()

    # Debug: Inspect y_test and y_pred
    print("y_test shape:", y_test.shape)
    print("y_pred shape:", y_pred.shape)
    print("y_test sample:", y_test[:5])
    print("y_pred sample:", y_pred[:5])

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Print the evaluation metrics
    print("Model Evaluation:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

def save_artifacts(model, pca, scaler, model_path, pca_path, scaler_path):
    """Save the trained model, PCA, and scaler to files."""
    joblib.dump(model, model_path)
    joblib.dump(pca, pca_path)
    joblib.dump(scaler, scaler_path)

# Main script
if __name__ == "__main__":
    # Load and preprocess data
    data = load_data("data/data.csv")
    X_train, X_test, y_train, y_test = preprocess_data(data)

    # Apply PCA
    X_train_pca, X_test_pca, pca, scaler = apply_pca(X_train, X_test, n_components=5)

    # Build and train the model
    model = build_model(X_train_pca, y_train)

    # Evaluate the model
    evaluate_model(model, X_test_pca, y_test)

    # Save the model, PCA, and scaler
    save_artifacts(model, pca, scaler, "models/model.pkl", "models/pca.pkl", "models/scaler.pkl")
    print("Model, PCA, and scaler saved successfully!")