"""
CODTECH Internship - House Price Prediction
Intern ID: CT-6212
Author: Rahul Yadav

This script performs data loading, basic cleaning, exploratory visualization,
model training and evaluation for house-price prediction.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import math

DATA_PATH = "data/house_prices.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Basic data cleaning
df = df.drop_duplicates()
df = df.dropna()

# Separate features and target
X = df.drop(columns=["price_lakh"])
y = df["price_lakh"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train Random Forest regression model
model = RandomForestRegressor(
    n_estimators=250,
    max_depth=12,
    random_state=42
)
model.fit(X_train, y_train)

# Predictions and evaluation
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
rmse = math.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print(f"MAE : {mae:.2f} lakh")
print(f"RMSE: {rmse:.2f} lakh")
print(f"R2  : {r2:.4f}")

# Actual vs predicted plot
plt.figure(figsize=(7, 5))
plt.scatter(y_test, predictions, alpha=0.65)
low = min(y_test.min(), predictions.min())
high = max(y_test.max(), predictions.max())
plt.plot([low, high], [low, high], linestyle="--")
plt.xlabel("Actual Price (Lakh)")
plt.ylabel("Predicted Price (Lakh)")
plt.title("Actual vs Predicted House Prices")
plt.tight_layout()
plt.show()
