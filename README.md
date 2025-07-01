# 📉 S&P 500 Historical Data Analysis  
A Python program for reading, validating, and visualizing over six decades of historical S&P 500 stock data using NumPy and Matplotlib.

---

## 📌 Overview  
**Author:** Khanh Nguyen  
**Language:** Python  
**Tools Used:** NumPy, Matplotlib  
**Dataset Source:** CSV file: `sp500_1950-01-03_to_2016-10-07.csv`  
**Date Range:** Jan 3, 1950 – Oct 7, 2016

---

## 🧠 Objective  
To manually process historical market data, validate array consistency across loading methods, and visualize both adjusted closing prices and daily trading ranges.

---

## 🛠 Code Workflow  

### ✅ Task 1: `convert_date_to_float()`  
- Converts date strings (`YYYY-MM-DD`) to float format (`YYYYMMDD.0`)

### ✅ Task 2:  
- Manually loads CSV data row by row into `data2` (excluding header)  
- Replaces `'null'` with `np.nan`

### ✅ Task 3:  
- Uses `np.genfromtxt()` to load the same data into `data3`

### ✅ Task 4:  
- Compares `data2[:, 1:]` and `data3[:, 1:]` using `np.allclose()`  
- Confirms manual and auto methods yield consistent numerical results

### ✅ Task 5:  
- Plots adjusted close price over time

### ✅ Task 6:  
- Plots daily high minus low price (volatility metric)

---

## 📈 Visual Output  
- Line plot: Adjusted Close vs Trading Days  
- Line plot: Daily High – Low vs Trading Days

---

## 📎 File Structure  
<pre><code>
├── sp500_1950-01-03_to_2016-10-07.csv # Raw S&P 500 historical data
├── S&P 500 Historical Data Analysis.py # Script with tasks 1–6
├── README.md
</code></pre>

---

## 📚 Conclusion  
This project illustrates foundational techniques in numerical data handling, error-tolerant loading, and time series plotting. It i
