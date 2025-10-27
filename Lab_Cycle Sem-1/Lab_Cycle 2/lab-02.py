import pandas as pd
import numpy as np

df=pd.read_csv("Lab_Cycle Sem-1\Lab_Cycle 2\Auto.csv")

print(df.head())

df['horsepower'] =df['horsepower'].replace('?',np.nan)

df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')

df = df.dropna(subset=['horsepower','mpg','displacement','weight','acceleration'])

df['company'] = df['name'].apply(lambda x: x.split()[0].lower())

company_counts=df['name'].value_counts()
print("\nTotal number of cars by company:", company_counts)

company_avg_mpg = df.groupby('company')['mpg'].mean().sort_values(ascending=False)
print("\nAverage mileage (mpg) by company:", company_avg_mpg)