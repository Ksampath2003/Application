import pandas as pd
import matplotlib.pyplot as plt

# Load Bitcoin data (Ensure you have a CSV with Date, Price, Volume, Market Cap)
df = pd.read_csv("bitcoin_data.csv", parse_dates=["Date"])
df.sort_values("Date", inplace=True)

# Set Date as index for easy plotting
df.set_index("Date", inplace=True)

# Plot Bitcoin Price Over Time
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Price"], label="Bitcoin Price", color="orange")
plt.xlabel("Year")
plt.ylabel("Price (USD)")
plt.title("Bitcoin Price History")
plt.legend()
plt.grid()
plt.show()

# Plot Bitcoin Trading Volume Over Time
plt.figure(figsize=(10, 5))
plt.bar(df.index, df["Volume"], label="Trading Volume", color="blue", alpha=0.6)
plt.xlabel("Year")
plt.ylabel("Volume (USD)")
plt.title("Bitcoin Trading Volume Over Time")
plt.legend()
plt.grid()
plt.show()

# Plot Bitcoin Market Capitalization Over Time
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Market Cap"], label="Market Capitalization", color="green")
plt.xlabel("Year")
plt.ylabel("Market Cap (USD)")
plt.title("Bitcoin Market Capitalization Over Time")
plt.legend()
plt.grid()
plt.show()

