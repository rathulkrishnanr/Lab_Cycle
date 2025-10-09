import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns


# Load the CSV file
df = pd.read_csv("iris.csv")


print("Head of the dataset:",df.head())
print("\nTail of the dataset:",df.tail())

# Mean of numeric columns
print("\nMean:\n", df.mean(numeric_only=True))

# Median of numeric columns
print("\nMedian:\n", df.median(numeric_only=True))

# Mode of each column (may return multiple modes per column)
print("\nMode:\n", df.mode(numeric_only=True))

df_dropped = df.dropna()
print("\nData after dropping missing values (head):\n", df_dropped.head())
print("\nData after dropping missing values (tail):\n", df_dropped.tail())
