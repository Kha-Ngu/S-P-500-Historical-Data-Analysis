# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 09:00:03 2025

S&P 500 Historical Data Analysis
--------------------------------

This program reads historical stock data for the S&P 500 index from a CSV file
containing trading data from January 3, 1950 to October 7, 2016. It performs the following tasks:

1. Defines a function to convert date strings in 'yyyy-mm-dd' format to floating point values.
2. Manually reads the file into a 2D NumPy array (`data2`) without using pre-built functions like genfromtxt.
3. Loads the same file again using NumPy's genfromtxt into `data3` for comparison.
4. Compares `data2` and `data3` to ensure all numeric values (except the date column) match.
5. Plots the adjusted closing price versus trading day.
6. Plots the daily difference between high and low prices versus trading day.

All plots are displayed using `matplotlib.pyplot`.

@author: khanh
"""

import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------
# Task 1: Define the function to convert date string to float
#----------------------------------------------------

def convert_date_to_float(date_str):
    """
    Converts a date string in 'yyyy-mm-dd' format to a float of the form yyyymmdd.0.

    Parameters:
        date_str (str): A string representing the date (e.g., '1950-01-03').

    Returns:
        float: The date converted to a numeric format (e.g., 19500103.0).
    """
    return float(date_str.replace('-', ''))

#----------------------------------------------------
# Task 2: Read file into 2D float array called data2
# Do not use genfromtxt or any other pre-written loading functions
#----------------------------------------------------

data2 = [] # Hold the final 2D float array
file = open('sp500_1950-01-03_to_2016-10-07.csv', 'r') # Open file for reading
try:
    header = file.readline() # Skip the header line
    for line in file:
        line = line.strip() # Remove newline and spaces
        columns = line.split(',')      
        # Convert the date string to float
        data_float = convert_date_to_float(columns[0])      
        # Convert remaining values to float or NaN
        values = []
        for val in columns[1:]:
            if val.lower() == 'null':
                values.append(np.nan)
            else:
                values.append(float(val))      
        # Combine date with values and add to list
        row = [data_float] + values
        data2.append(row)    
except FileNotFoundError:
    print("Error: The file was not found")
except ValueError:
    print("Error converting data to float:", ValueError)
except Exception:
    print("An unexpected error occured:", Exception)
finally:
    # Close file
    file.close()
# Convert to NumPy array after reading
data2 = np.array(data2)

#-------------------------------------------------------
# Task 3: Reads the contents of the data file into a 2-D 
# floating point array data3 using genfromtxt
#-------------------------------------------------------

data3 = np.genfromtxt( 'sp500_1950-01-03_to_2016-10-07.csv',
    delimiter=',',
    skip_header=1,
    dtype=float
)

#--------------------------------------------------------------
# Task 4: Compare all values (except the first column) in data2 
# and data3 to confirm they are "equal" to each other. 
#--------------------------------------------------------------

if data2.size != data3.size:
    print('data2 and data3 arrays are not equal to each other.') 
else:
    are_close = np.allclose(data2[:, 1:], data3[:, 1:], equal_nan=True)
    print('Comparison Result (excluding dates):', are_close)
    
#-----------------------------------------------------------------
# Task 5: Create an x-y plot of the adjusted close (y-axis) versus 
# trading day (x-axis)
#-----------------------------------------------------------------

plt.figure()
plt.plot(range(len(data2)), data2[:, -1], color='blue')
plt.title("S&P 500 Index Daily Close")
plt.xlabel("Trading Days Since Jan 3, 1950")
plt.ylabel("Adjusted Close [USD]")
plt.grid(True)

# --------------------------------------------------
# Task 6: Plot Daily High - Low vs Trading Days
# --------------------------------------------------

# High is column 2, Low is column 3
daily_high_minus_low = data2[:, 2] - data2[:, 3]
plt.figure()
plt.plot(range(len(data2)), daily_high_minus_low, color='blue')
plt.title("S&P 500 Index Daily High Minus Low")
plt.xlabel("Trading Days Since Jan 3, 1950")
plt.ylabel("Daily High-Low [USD]")
plt.grid(True)
plt.show()














