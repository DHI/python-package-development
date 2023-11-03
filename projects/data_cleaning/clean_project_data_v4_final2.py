import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Create date range
date_rng = pd.date_range(start="1/1/2020", end="1/31/2020", freq="D")

# Sample time series data with DateTimeIndex
data1 = pd.Series([1, 2, -1, 4, 5, 20, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                   21, 22, 24, 24, 24, 24, 24, 24, 29, 30, 31], index=date_rng)
data2 = pd.Series([5, 6, 200, 8, 9, 10, 11, 12, 300, 14, 15, 16, 17, 18, 19, 20, 21, 22, 
                   23, 24, 25, 26, 27, 27, 27, 30, 31, 32, 33, 34, 35], index=date_rng)
data3 = pd.Series([15, 16, 11, 18, 400, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
                   32, 33, 34, 35, 36, 37, 38, 39, 45, 45, 45, 45, 45, 45], index=date_rng)


# Cleaning data1
print("\nCleaning data1")
data1_original = data1.copy()

# Checking for jumps 
print("Checking for jumps in data1")
max_jump=10
prev_value = data1.iloc[0]
for t, value in data1.items():
    if abs(value - prev_value) <= max_jump:
        # "Value ok"
        data1[t] = value
        prev_value = value
    else:
        data1[t] = np.nan
        print("Jump detected and value removed on", t, ":", value)
print(f"Data removed: {data1_original[~data1_original.isin(data1)]}")
# print("Data1 after jump check:", data1)

# Checking for values in range 
min_val = 0
max_val = 50
for t, value in data1.items():
    # print("Checking value on", t, ":", value)
    if min_val <= value <= max_val:
        pass
        # print("Value ok:", value)
    else:
        data1[t] = np.nan
        print("Value removed:", value)
print(f"Data removed: {data1_original[~data1_original.isin(data1)]}")
# print("Data1 after range check:", data1)


# Checking for flat periods 
print("Checking for flat periods in data1")
flat_period = 5
i = 0
while i < len(data1) - flat_period:
    if len(set(data1[i: i + flat_period + 1])) == 1: 
        print("Removing flat period starting at index:", i)
        data1[i: i + flat_period + 1] = np.nan
        i += flat_period
    else:
        i += 1
print(f"Data removed: {data1_original[~data1_original.isin(data1)]}")
# print("Data1 after flat period check:", data1)


# Cleaning data2
print("\nCleaning data2")
data2_original = data2.copy()

# Checking for jumps 
print("Checking for jumps in data2")
max_jump=10
prev_value = data2.iloc[0]
for t, value in data2.items():
    if abs(value - prev_value) <= max_jump:
        # "Value ok"
        data2[t] = value
        prev_value = value
    else:
        data2[t] = np.nan
        print("Jump detected and value removed on", t, ":", value)
print(f"Data removed: {data2_original[~data2_original.isin(data2)]}")
# print("data2 after jump check:", data2)

# Checking for values in range 
min_val = 0
max_val = 50
for t, value in data2.items():
    # print("Checking value on", t, ":", value)
    if min_val <= value <= max_val:
        pass
        # print("Value ok:", value)
    else:
        data2[t] = np.nan
        print("Value removed:", value)
print(f"Data removed: {data2_original[~data2_original.isin(data2)]}")
# print("data2 after range check:", data2)


# Checking for flat periods 
print("Checking for flat periods in data2")
flat_period = 5
i = 0
while i < len(data2) - flat_period:
    if len(set(data2[i: i + flat_period + 1])) == 1: 
        print("Removing flat period starting at index:", i)
        data2[i: i + flat_period + 1] = np.nan
        i += flat_period
    else:
        i += 1
print(f"Data removed: {data2_original[~data2_original.isin(data2)]}")
# print("data2 after flat period check:", data2)

# print("Final cleaned data2:", data2)

# Cleaning data3
print("\nCleaning data3")
data3_original = data3.copy()

# Checking for jumps 
print("Checking for jumps in data3")
max_jump=10
prev_value = data3.iloc[0]
for t, value in data3.items():
    if abs(value - prev_value) <= max_jump:
        # "Value ok"
        data3[t] = value
        prev_value = value
    else:
        data3[t] = np.nan
        print("Jump detected and value removed on", t, ":", value)
print(f"Data removed: {data3_original[~data3_original.isin(data3)]}")
# print("data3 after jump check:", data3)

# Checking for values in range 
min_val = 0
max_val = 50
for t, value in data3.items():
    # print("Checking value on", t, ":", value)
    if min_val <= value <= max_val:
        pass
        # print("Value ok:", value)
    else:
        data3[t] = np.nan
        print("Value removed:", value)
print(f"Data removed: {data3_original[~data3_original.isin(data3)]}")
# print("data3 after range check:", data3)


# Checking for flat periods 
print("Checking for flat periods in data3")
flat_period = 5
i = 0
while i < len(data3) - flat_period:
    if len(set(data3[i: i + flat_period + 1])) == 1: 
        print("Removing flat period starting at index:", i)
        data3[i: i + flat_period + 1] = np.nan
        i += flat_period
    else:
        i += 1
print(f"Data removed: {data3_original[~data3_original.isin(data3)]}")
# print("data3 after flat period check:", data3)

# print("Final cleaned data3:", data3)

## plot data showing outliers as red dots
plt.figure(figsize=(10, 5))
plt.plot(data1_original, '.', color="red")
plt.plot(data1, '.', color="green")
plt.title("Data1")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(data2_original, '.', color="red")
plt.plot(data2, '.', color="green")
plt.title("Data2")
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(data3_original, '.', color="red")
plt.plot(data3, '.', color="green")
plt.title("Data3")
plt.show()