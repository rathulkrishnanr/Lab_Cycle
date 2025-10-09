import numpy as np

item1 = input("Enter element for first list: ")
item2 = input("Enter element for second list: ")

list1 = list(map(int, item1.split()))
list2 = list(map(int, item2.split()))

# Step 1: Create a NumPy array
arr1 = np.array(list1)
arr2 = np.array(list2)

# Step 2: Element-wise operations
addition = arr1 + arr2
multiplication = arr1 * arr2

# Step 3: Statistical operations
mean_val = np.mean(arr1)
variance_val = np.var(arr1)
std_dev_val = np.std(arr1)

# Display results
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Element-wise Addition:", addition)
print("Element-wise Multiplication:", multiplication)
print("Mean of arr1:", mean_val)
print("Variance of arr1:", variance_val)
print("Standard Deviation of arr1:", std_dev_val)
