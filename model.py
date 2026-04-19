import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("cleaned_bitcoin.csv")

# Features & target
X = df[['MA_7', 'MA_30', 'Volatility']]
y = df['Close']

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
df['Predicted_Price'] = model.predict(X)

# Save predictions
df.to_csv("predictions.csv", index=False)

print("✅ Model trained & predictions saved!")