import matplotlib.pyplot as plt

# Sample data
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [25, 40, 30, 10]

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='skyblue')
plt.title('Fruit Sales')
plt.xlabel('Fruit')
plt.ylabel('Quantity Sold')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
