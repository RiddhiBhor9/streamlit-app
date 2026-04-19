import pandas as pd

# Load dataset
df = pd.read_csv("coin_Bitcoin.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Sort values
df = df.sort_values('Date')

# Feature Engineering
df['Daily_Return'] = df['Close'].pct_change()
df['MA_7'] = df['Close'].rolling(window=7).mean()
df['MA_30'] = df['Close'].rolling(window=30).mean()
df['Volatility'] = df['Daily_Return'].rolling(window=7).std()

# Drop null values
df = df.dropna()

# Save cleaned data
df.to_csv("cleaned_bitcoin.csv", index=False)

print("✅ Data cleaned and saved!")