📈 Time Series Sales Forecasting (Superstore Dataset)
📌 Project Overview

This project focuses on time series analysis and forecasting using historical sales data from a retail Superstore dataset.
The goal is to:

Analyze long-term sales trends

Decompose the time series into components

Build an ARIMA model

Forecast future sales for the next 12 months

🗂 Dataset

Source: Superstore sales dataset

File: data/superstore.csv

Records: 9,994 rows × 21 columns

Target Variable: Sales

Date Column: Order Date

⚙️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Statsmodels

Scikit-learn

🔍 Steps Performed
1️⃣ Data Preprocessing

Loaded CSV file

Converted Order Date to datetime

Set date as index

Resampled data to monthly total sales

2️⃣ Exploratory Time Series Analysis

Visualized monthly sales trend

Observed upward trend with fluctuations

3️⃣ Time Series Decomposition

Decomposed the series into:

Trend

Seasonal

Residual

This helped understand underlying patterns in sales.

4️⃣ Model Building (ARIMA)

Built an ARIMA(1,1,1) model

Evaluated model using AIC and residual diagnostics

5️⃣ Forecasting

Forecasted sales for the next 12 months (2019)

Generated future sales predictions

📊 Results
🔹 Forecasted Sales (Next 12 Months)
2019-01-31    75259
2019-02-28    73306
2019-03-31    72862
2019-04-30    72760
2019-05-31    72737
2019-06-30    72732
2019-07-31    72731
2019-08-31    72731
2019-09-30    72730
2019-10-31    72730
2019-11-30    72730
2019-12-31    72730
📈 Key Insight

Sales are expected to:

Slightly decline initially

Then stabilize around ~72,730 per month

📁 Project Structure
project3_time_series_forecasting/
│
├── data/
│   └── superstore.csv
│
├── project3_time_series_forecasting.py
├── requirements.txt
└── README.md
🚀 How to Run the Project
1️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the script
python project3_time_series_forecasting.py
📌 Skills Demonstrated

Time series preprocessing

Data resampling

Trend & seasonality analysis

ARIMA modeling

Forecasting

Data visualization

🧠 Business Use Case

This model can help businesses:

Predict future revenue

Plan inventory

Detect long-term sales trends

Support data-driven decision making

✨ Future Improvements

Implement Seasonal ARIMA (SARIMA)

Add confidence intervals to forecasts

Compare with Prophet or LSTM models

Add automated parameter tuning (auto_arima)