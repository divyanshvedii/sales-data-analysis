import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('data.csv')

# Display first 5 rows
print("----- Data Preview -----")
print(data.head())

# Total Sales
total_sales = data['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Best Selling Product
product_sales = data.groupby('Product')['Sales'].sum()
best_product = product_sales.idxmax()
print("Best Selling Product:", best_product)

# Sales by Region
region_sales = data.groupby('Region')['Sales'].sum()
print("\n----- Sales by Region -----")
print(region_sales)

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Extract Month
data['Month'] = data['Date'].dt.month

# Monthly Sales
monthly_sales = data.groupby('Month')['Sales'].sum()

print("\n----- Monthly Sales -----")
print(monthly_sales)

# 📊 Plot 1: Monthly Sales Trend
plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.grid()
plt.show()

# 📊 Plot 2: Sales by Region (Bar Chart)
plt.figure()
region_sales.plot(kind='bar')
plt.xlabel("Region")
plt.ylabel("Sales")
plt.title("Sales by Region")
plt.grid()
plt.show()

# 📊 Plot 3: Sales by Product (Pie Chart)
plt.figure()
product_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Product")
plt.ylabel("")
plt.show()