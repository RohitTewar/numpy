import numpy as np
import matplotlib.pyplot as plt

# Data : [restaurant_name, 2020, 2021, 2022, 2023]
sales_data = np.array([
    [1, 150000, 180000, 200000, 220000],  #'Pizza Point'
    [2, 120000, 140000, 160000, 180000],  #'Chai Lovers'  
    [3, 100000, 120000, 140000, 160000],  #'Sutta Bar'
    [4, 80000, 90000, 100000, 110000],    #'NBC'
    [5, 60000, 70000, 80000, 90000]       #'Dosa Point'

])
print("==== Sales analysis ====")
print("\n sales data shape:", sales_data.shape)
print("\n sample data of 1st 2 restaurant:\n", sales_data[:2])

#total sales per year
print(np.sum(sales_data, axis=0))

yearly_total = np.sum(sales_data[:, 1:], axis=0)
print(yearly_total)

#minimum sales per year
min_sales =np.min(sales_data[:, 1:], axis=1)
print("\n min sales",min_sales)

#maximum sales per year
max_sales =np.max(sales_data[:,1:], axis= 0)
print("\n max sales", max_sales)

#average sales per year
avg_sales = np.mean(sales_data[:, 1:], axis=1)
print("\n avg sales", avg_sales)

cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print("\n cumulative sum of sales:\n", cumsum)

plt.figure(figsize=(10, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title("Average Cumulative Sales Over Years")
plt.xlabel("Years")
plt.ylabel("Cumulative Sales")
plt.grid(True)
plt.show()

# vector addition
v1 = np.array([1,2,3,4,5])
v2 = np.array([5,7,8,9,10])
print("\n vector addition:", v1 + v2)

#vector multiplication
print("\n vector multiplication:", v1 * v2)

#vector dot product
print("\n vector dot product:", np.dot(v1, v2))

#angle in degrees
angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
print("\n angle between v1 and v2 in radians:", angle)

# Vectorized string operations
restaurant_types = np.array(['Pizza Point', 'Chai Lovers', 'Sutta Bar', 'NBC', 'Dosa Point'])
vectorized_upper = np.vectorize(str.upper)
print("\n Restaurant names in uppercase:", vectorized_upper(restaurant_types))

# Vectorized operations on sales data
monthly_avg = sales_data[:, 1:] / 12
print("\n Monthly average sales:\n", monthly_avg)