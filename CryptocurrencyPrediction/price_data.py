import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load datasets
price_data = pd.read_csv("crypto_price_data.csv")
sentiment_data = pd.read_csv("social_media_sentiment.csv")

# Convert timestamp columns to datetime
price_data["timestamp"] = pd.to_datetime(price_data["timestamp"])
sentiment_data["timestamp"] = pd.to_datetime(sentiment_data["timestamp"])

# Merge datasets on timestamp
merged_data = pd.merge(price_data, sentiment_data, on="timestamp", how="inner")

# Handle missing values (if any)
merged_data.fillna(method="ffill", inplace=True)  # Forward fill missing values

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(merged_data[["price", "sentiment"]])

# Create a new DataFrame with scaled data
scaled_df = pd.DataFrame(scaled_data, columns=["price_scaled", "sentiment_scaled"])
scaled_df["timestamp"] = merged_data["timestamp"]

# Save preprocessed data
scaled_df.to_csv("preprocessed_data.csv", index=False)
print("Data preprocessing complete. File saved.")
