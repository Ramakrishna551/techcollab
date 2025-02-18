import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load sensor data (assuming CSV file with columns: 'timestamp', 'sensor_reading', 'vehicle_count')
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Preprocess data
def preprocess_data(data):
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['hour'] = data['timestamp'].dt.hour
    features = ['sensor_reading', 'hour']
    target = 'vehicle_count'
    X = data[features]
    y = data[target]
    return X, y

# Train model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    return model, scaler

# Predict vehicle count
def predict_vehicle_count(model, scaler, sensor_reading, hour):
    input_data = np.array([[sensor_reading, hour]])
    input_scaled = scaler.transform(input_data)
    return model.predict(input_scaled)[0]

if __name__ == "__main__":
    file_path = 'sensor_data.csv'  # Update with actual file path
    data = load_data(file_path)
    X, y = preprocess_data(data)
    model, scaler = train_model(X, y)
    test_prediction = predict_vehicle_count(model, scaler, 30.5, 14)  # Example input
    print("Predicted Vehicle Count:", test_prediction)
