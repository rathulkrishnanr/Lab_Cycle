import pandas as pd
import matplotlib.pyplot as plt

# Load the retail sales profits data - Use raw string (r prefix)
df = pd.read_csv(r'D:\Lab_Cycle\Lab_Cycle Sem-1\Lab_Cycle 2\retail_sales_profits.csv')

# Prepare category-level summaries
category_summary = df.groupby('Store Category').agg({
    'Q3 Sales ($)': 'sum',
    'Q3 Profit ($)': 'sum',
    'Q4 Sales ($)': 'sum',
    'Q4 Profit ($)': 'sum'
}).reset_index()

# a) Quarterly Profit Comparison - Line Chart
plt.figure(figsize=(12, 6))
plt.plot(category_summary['Store Category'], category_summary['Q3 Profit ($)'], 
         marker='o', linewidth=2, markersize=8, label='Q3 Profit')
plt.plot(category_summary['Store Category'], category_summary['Q4 Profit ($)'], 
         marker='s', linewidth=2, markersize=8, label='Q4 Profit')
plt.title('Quarterly Profit Comparison (Q3 vs Q4)', fontsize=16, fontweight='bold')
plt.xlabel('Store Category', fontsize=12)
plt.ylabel('Profit ($)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# b) Category Sales Comparison - Grouped Bar Chart
plt.figure(figsize=(14, 6))
x = range(len(category_summary['Store Category']))
width = 0.35
plt.bar([i - width/2 for i in x], category_summary['Q3 Sales ($)'], 
        width, label='Q3 Sales', alpha=0.8)
plt.bar([i + width/2 for i in x], category_summary['Q4 Sales ($)'], 
        width, label='Q4 Sales', alpha=0.8)
plt.title('Category Sales Comparison (Q3 vs Q4)', fontsize=16, fontweight='bold')
plt.xlabel('Store Category', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.xticks(x, category_summary['Store Category'])
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# c) Total Sales Distribution - Pie Chart
plt.figure(figsize=(10, 8))
category_summary['Total Sales'] = category_summary['Q3 Sales ($)'] + category_summary['Q4 Sales ($)']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#96CEB4']
explode = (0, 0, 0.05, 0, 0)  # Explode Electronics (largest)
plt.pie(category_summary['Total Sales'], labels=category_summary['Store Category'], 
        autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, 
        shadow=True, textprops={'fontsize': 12})
plt.title('Total Sales Distribution by Category', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()

print("\nAll visualizations created successfully!")
print(f"\nSummary Statistics:")
print(category_summary[['Store Category', 'Q3 Sales ($)', 'Q4 Sales ($)', 'Total Sales']])

