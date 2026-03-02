import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
# Load dataset
df = pd.read_csv("data/superstore.csv")

print(df.head())
print(df.shape)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Set Order Date as index
df = df.set_index("Order Date")

# Sort by date (important for time series)
df = df.sort_index()

# Aggregate sales by month
monthly_sales = df["Sales"].resample("M").sum()

print(monthly_sales.head())

# Plot time series
plt.figure(figsize=(10,5))
plt.plot(monthly_sales)
plt.title("Monthly Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

# Decompose time series
decomposition = seasonal_decompose(monthly_sales, model="additive")

# Plot decomposition
decomposition.plot()
plt.show()

# Train ARIMA model (p,d,q)
model = ARIMA(monthly_sales, order=(1,1,1))
model_fit = model.fit()

print(model_fit.summary())

# Forecast next 12 months
forecast = model_fit.forecast(steps=12)

print("Forecasted Sales for Next 12 Months:")
print(forecast)

# Plot forecast
plt.figure(figsize=(10,5))
plt.plot(monthly_sales, label="Historical Sales")
plt.plot(forecast, label="Forecast", color="red")
plt.legend()
plt.title("Sales Forecast for Next 12 Months")
plt.show()