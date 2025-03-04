import requests
import pandas as pd
import datetime

# Function to fetch historical price data from CoinGecko API
def fetch_crypto_price_data(crypto_id, start_date, end_date):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart/range"
    params = {
        "vs_currency": "usd",
        "from": int(start_date.timestamp()),
        "to": int(end_date.timestamp())
    }
    response = requests.get(url, params=params)
    data = response.json()
    prices = data["prices"]
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    return df

# Function to fetch social media sentiment data (mock example using Twitter API)
def fetch_social_media_sentiment(query, start_date, end_date):
    # Mock implementation (replace with actual API calls)
    print(f"Fetching sentiment data for query: {query} from {start_date} to {end_date}")
    dates = pd.date_range(start_date, end_date)
    sentiment = [0.5, -0.2, 0.7, -0.1, 0.3]  # Mock sentiment scores
    df = pd.DataFrame({"timestamp": dates, "sentiment": sentiment})
    return df

# Main execution
if __name__ == "__main__":
    crypto_id = "bitcoin"
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 10, 1)

    # Fetch data
    price_data = fetch_crypto_price_data(crypto_id, start_date, end_date)
    sentiment_data = fetch_social_media_sentiment("Bitcoin", start_date, end_date)

    # Save data to CSV
    price_data.to_csv("crypto_price_data.csv", index=False)
    sentiment_data.to_csv("social_media_sentiment.csv", index=False)
    print("Data collection complete. Files saved.")
