import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Line Graph: y = x^2
x = np.linspace(-10, 10, 400)
y = x**2

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = x^2', color='blue')
plt.title('Line Graph of y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# Read data from CSV
df = pd.read_csv('iris.csv')
grouped = df.groupby('variety')['sepal.length'].mean()

# Bar Chart 
plt.figure(figsize=(8, 5))
plt.bar(grouped.index, grouped.values, color='orange')
plt.title('Iris Bar Chart')
plt.xlabel('variety')
plt.ylabel('Average Sepal Length')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['sepal.length'],bins=10, color='green', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()