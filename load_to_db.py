from sqlalchemy import create_engine
import pandas as pd

# Update with your PostgreSQL credentials
username = "postgres"
password = "shree@09"
host = "localhost"
port = "5432"
database = "crypto_db"
engine = create_engine("postgresql://postgres:shree09@localhost:5432/YOUR_DB")

# Load cleaned data
df = pd.read_csv("cleaned_bitcoin.csv")

# Upload to DB
df.to_sql("bitcoin_prices", engine, if_exists="replace", index=False)

print("✅ Data loaded into PostgreSQL!")

import psycopg2
print("Installed successfully")