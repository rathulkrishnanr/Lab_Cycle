import pandas as pd
import matplotlib.pyplot as plt

data ={
    "SN":[1, 2,3 ],
    "Name":["Linus Torvalds",
            "Tim Berners-Lee",
            "Guido van Rossum"],
    "Country":["Finland",
               "England",
               "Netherlands"],
    "Contribution":["Linux",
                    "World wide Web",
                    "Python"],
    "Year":[1991,1990,1991]
}

df = pd.DataFrame(data)
df.to_csv("contributors.csv", index= False)

print("Data written to contributors.csv")

#Company Sales
companydata ={
    "MonthNumber":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "FaceCream":[2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    "FaceWash":[1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    "ToothPaste":[5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    "BathingSoap":[9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    "Shampoo":[1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    "Moisturizer":[1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
}

companydata["TotelUnit"] = []
companydata["TotelProfilt"] = []

for i in range(12):
    total = (companydata["FaceCream"][i]+companydata["FaceWash"][i]+companydata["ToothPaste"][i]+companydata["BathingSoap"][i]+companydata["Shampoo"][i]+companydata["Moisturizer"][i])
    companydata["TotelUnit"].append(total)
    companydata["TotelProfilt"].append(total*0.30)

df = pd.DataFrame(companydata)
df.to_csv("company.csv", index= False)

# a) Toothpaste Sales - Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df["MonthNumber"],df["ToothPaste"],s=100,alpha=0.7)
plt.title('ToothPaste Sales by Month', fontsize=14,fontweight='bold')
plt.xlabel('Month Number',fontsize=12)
plt.ylabel('Sales Units', fontsize=12)
plt.grid()
plt.show()
print("Toothpaste scatter plot created")

# b) Face Cream and Face Wash - Bar Chart
plt.figure(figsize=(12,6))
x= df["MonthNumber"]
width=0.35
plt.bar(x - width/2, df['FaceCream'], width, label='Face Cream', alpha=0.8)
plt.bar(x + width/2, df['FaceWash'], width, label='Face Wash', alpha=0.8)
plt.title('Face Cream vs Face Wash Sales', fontsize=14, fontweight='bold')
plt.xlabel('Month Number', fontsize=12)
plt.ylabel('Sales Units', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
print("Face products bar chart created")

# c) Total Sales by Product - Pie Chart
plt.figure(figsize=(10, 8))
total_sales = {
    'Face Cream': df['FaceCream'].sum(),
    'Face Wash': df['FaceWash'].sum(),
    'Toothpaste': df['ToothPaste'].sum(),
    'Bathing Soap': df['BathingSoap'].sum(),
    'Shampoo': df['Shampoo'].sum(),
    'Moisturizer': df['Moisturizer'].sum()
}

products = list(total_sales.keys())
sales = list(total_sales.values())

plt.pie(sales, labels=products, autopct='%1.1f%%', startangle=90)
plt.title('Total Sales Distribution by Product (Last Year)', fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()
print("Product sales pie chart created")