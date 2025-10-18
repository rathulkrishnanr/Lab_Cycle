import pandas as pd
import matplotlib.pyplot as plt

# Load the sample sales dataset
df = pd.read_csv('D:\Lab_Cycle\Lab_Cycle Sem-1\Lab_Cycle 2\Sales_Dataset.csv')

# Parse dates and extract month information
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['MonthName'] = df['Order Date'].dt.strftime('%B')

# Aggregate monthly data
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

monthly_data = df.groupby('MonthName').agg({
    'Amount': 'sum',
    'Profit': 'sum'
}).reset_index()

monthly_data['month_num'] = monthly_data['MonthName'].apply(lambda x: month_order.index(x))
monthly_data = monthly_data.sort_values('month_num').reset_index(drop=True)

# Category-wise data
category_data = df.groupby('Category').agg({
    'Amount': 'sum'
}).reset_index()

# a) Monthly Profit - Line Chart
plt.figure(figsize=(12, 6))
plt.plot(monthly_data['MonthName'], monthly_data['Profit'], 
         marker='o', linewidth=2.5, markersize=8, color='#2E86AB')
plt.title('Monthly Profit Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Profit ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.show()

# b) Electronics and Furniture Sales - Grouped Bar Chart
electronics_monthly = df[df['Category'] == 'Electronics'].groupby('MonthName')['Amount'].sum()
furniture_monthly = df[df['Category'] == 'Furniture'].groupby('MonthName')['Amount'].sum()

# Reindex to ensure all months are present
electronics_monthly = electronics_monthly.reindex(month_order, fill_value=0)
furniture_monthly = furniture_monthly.reindex(month_order, fill_value=0)

plt.figure(figsize=(14, 6))
x = range(len(month_order))
width = 0.35
plt.bar([i - width/2 for i in x], electronics_monthly.values, 
        width, label='Electronics', alpha=0.85, color='#FF6B6B')
plt.bar([i + width/2 for i in x], furniture_monthly.values, 
        width, label='Furniture', alpha=0.85, color='#4ECDC4')
plt.title('Electronics vs Furniture Sales Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.xticks(x, month_order, rotation=45, ha='right')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3, axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# c) Total Yearly Sales by Category - Pie Chart
plt.figure(figsize=(10, 8))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
explode = (0, 0.05, 0)  # Explode Furniture (middle slice)
plt.pie(category_data['Amount'], labels=category_data['Category'], 
        autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, 
        shadow=True, textprops={'fontsize': 13, 'fontweight': 'bold'})
plt.title('Total Yearly Sales by Category', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

print("\nAll visualizations created successfully!")
print(f"\nTotal Sales by Category:")
print(category_data)
print(f"\nMonthly Summary:")
print(monthly_data[['MonthName', 'Amount', 'Profit']])
