# 📈 Project 3: Superstore Sales Forecasting (ARIMA)

## 📌 Overview
This project performs **time series analysis and forecasting** on Superstore sales data using an **ARIMA model**.  
The goal is to predict future monthly sales based on historical trends.

---

## 🗂 Dataset
**File:** `data/superstore.csv`  
**Target Column:** `Sales`  
**Date Column:** `Order Date`

The data is aggregated into **monthly sales** for modeling.

---

## ⚙️ Technologies Used
- Python  
- Pandas  
- Matplotlib  
- Statsmodels (ARIMA / SARIMAX)

---

## 📊 Model Summary
- Model: **ARIMA(1,1,1)**
- Observations: 48 months (2015–2018)
- Forecast Horizon: 12 months (2019)

---

## 🔮 Forecast Output
The model forecasts sales for the next 12 months:
- Shows a stable sales pattern around **72,730**

---

## 🧪 Steps Performed
1. Data cleaning & date parsing  
2. Monthly aggregation  
3. Stationarity check  
4. ARIMA modeling  
5. Model evaluation  
6. 12-month forecasting  
7. Visualization  

---

## ▶️ How to Run

```bash
pip install pandas matplotlib statsmodels
python project3_time_series_forecasting.py
```

---

## 📁 Project Structure

```
project3/
│
├── data/
│   └── superstore.csv
│
├── project3_time_series_forecasting.py
└── README.md
```

---

## 📌 Output
- Line chart of historical sales
- Forecasted sales for next 12 months
- Model diagnostics

---

## ✍️ Author
**Asif Iqbal**  
Senior .NET Developer & Data Science Learner  

---

⭐ If you like this project, give it a star!
