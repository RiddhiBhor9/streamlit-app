import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Crypto Analytics Dashboard")

# Load data
df = pd.read_csv("predictions.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar filter
start_date = st.sidebar.date_input("Start Date", df['Date'].min())
end_date = st.sidebar.date_input("End Date", df['Date'].max())

filtered_df = df[(df['Date'] >= str(start_date)) & (df['Date'] <= str(end_date))]

# Price Chart
st.subheader("📈 Price Trend")

plt.figure()
plt.plot(filtered_df['Date'], filtered_df['Close'], label="Actual Price")
plt.plot(filtered_df['Date'], filtered_df['Predicted_Price'], label="Predicted Price")
plt.legend()
st.pyplot(plt)

# Moving Average
st.subheader("📊 Moving Averages")

plt.figure()
plt.plot(filtered_df['Date'], filtered_df['MA_7'], label="MA 7")
plt.plot(filtered_df['Date'], filtered_df['MA_30'], label="MA 30")
plt.legend()
st.pyplot(plt)

# Show data
st.subheader("📄 Data Table")
st.dataframe(filtered_df)