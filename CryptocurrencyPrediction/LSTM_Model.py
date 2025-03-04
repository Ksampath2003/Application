import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.model_selection import train_test_split

# Load preprocessed data
data = pd.read_csv("preprocessed_data.csv")

# Prepare features and target
X = data[["price_scaled", "sentiment_scaled"]].values
y = data["price_scaled"].shift(-1).dropna().values  # Predict next day's price
X = X[:-1]  # Align features with target

# Reshape data for LSTM input (samples, timesteps, features)
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Compile the model
model.compile(optimizer="adam", loss="mean_squared_error")

# Train the model
model.fit(X_train, y_train, batch_size=32, epochs=20, validation_data=(X_test, y_test))

# Save the trained model
model.save("crypto_price_lstm_model.h5")
print("Model training complete. Model saved.")
