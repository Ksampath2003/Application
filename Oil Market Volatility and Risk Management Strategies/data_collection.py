import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# API key and URLs for EIA (Replace 'YOUR_API_KEY' with an actual API key from EIA)
EIA_API_KEY = "YOUR_API_KEY"
EIA_URL = f"https://api.eia.gov/series/?api_key={EIA_API_KEY}&series_id=PET.RWTC.D"

# Function to fetch oil price data from EIA
def fetch_eia_data():
    response = requests.get(EIA_URL)
    if response.status_code == 200:
        data = response.json()
        prices = data["series"][0]["data"]
        df = pd.DataFrame(prices, columns=["Date", "Price"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date")
        return df
    else:
        print("Failed to fetch data from EIA.")
        return None

# Function to plot and save oil price trends
def plot_oil_prices(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Price"], marker='o', linestyle='-', label="WTI Crude Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD per Barrel)")
    plt.title("Oil Price Trends (Last 3 Months)")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.savefig("oil_prices.png")
    plt.show()

# Main script execution
if __name__ == "__main__":
    oil_data = fetch_eia_data()
    if oil_data is not None:
        oil_data.to_csv("oil_prices.csv", index=False)
        plot_oil_prices(oil_data)
        print("Oil price data saved as 'oil_prices.csv' and plot saved as 'oil_prices.png'."
