#filter with mask
import numpy as np
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_numbers = numbers[numbers % 2 == 0]
print("Even numbers:", even_numbers)

mask = numbers> 5
print("Numbers greater than 5:", numbers[mask])

# Fancy indexing vs np.where
indices = [0, 2, 4, 6, 8]
print(numbers[indices]) 

where_result =np.where(numbers > 5) 
print(where_result)
print("np where", numbers[where_result])

condition_array = np.where(numbers>5,numbers *3,numbers)
print("Condition array:", condition_array) 

condition_array = np.where(numbers>5,"true","false")
print("Condition array:", condition_array) 