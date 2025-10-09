import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd


iris=pd.read_csv("iris.csv")
sns.scatterplot(
    x='sepal.length',
    y='sepal.width',
    hue='variety',
    data=iris,
    palette='Set1'
)
# Plot
plt.title('Iris')
plt.grid(True)
plt.show()
