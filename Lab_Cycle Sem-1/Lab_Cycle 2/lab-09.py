# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# ===========================
# 1. Load the Iris Dataset from CSV
# ===========================
iris_df = pd.read_csv('D:\Lab_Cycle\Lab_Cycle Sem-1\Lab_Cycle 2\iris.csv')

print("Dataset loaded from 'iris.csv' successfully!")
print("\nFirst 10 rows of the dataset:")
print(iris_df.head(10))

# Rename columns to match the requested format (using underscores)
iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

print("\nColumns renamed successfully!")
print("Updated column names:", iris_df.columns.tolist())
print("\nDataset shape:", iris_df.shape)

# ===========================
# 2. Clean the Dataset
# ===========================
print("\nChecking for missing values:")
print(iris_df.isnull().sum())

print("\nBasic statistics:")
print(iris_df.describe())

print("\nData types:")
print(iris_df.dtypes)

# ===========================
# 3. Manual Train-Test Split (80-20)
# ===========================

# Shuffle the dataset
iris_df_shuffled = iris_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Calculate split index (80% training, 20% testing)
train_size = int(0.8 * len(iris_df_shuffled))

# Split the data
train_df = iris_df_shuffled[:train_size]
test_df = iris_df_shuffled[train_size:]

# Separate features and target
X_train = train_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y_train = train_df['species']

X_test = test_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y_test = test_df['species']

print("\n" + "="*60)
print("DATASET SPLIT (80-20)")
print("="*60)
print(f"Training set size: {len(X_train)} samples (80%)")
print(f"Testing set size: {len(X_test)} samples (20%)")

# ===========================
# 4. Display Species Counts
# ===========================
print("\n" + "="*60)
print("NUMBER OF SAMPLES FOR EACH SPECIES (FULL DATASET)")
print("="*60)
species_counts = iris_df['species'].value_counts().sort_index()
for species, count in species_counts.items():
    print(f"{species}: {count} samples")

print("\n" + "="*60)
print("NUMBER OF SAMPLES FOR EACH SPECIES (TRAINING SET)")
print("="*60)
train_species_counts = y_train.value_counts().sort_index()
for species, count in train_species_counts.items():
    print(f"{species}: {count} samples")

print("\n" + "="*60)
print("NUMBER OF SAMPLES FOR EACH SPECIES (TESTING SET)")
print("="*60)
test_species_counts = y_test.value_counts().sort_index()
for species, count in test_species_counts.items():
    print(f"{species}: {count} samples")

# ===========================
# 5. Plot Histograms
# ===========================

# Create figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Histogram for Sepal Length
axes[0].hist(iris_df['sepal_length'], bins=20, color='skyblue', edgecolor='black')
axes[0].set_xlabel('Sepal Length (cm)', fontsize=12)
axes[0].set_ylabel('Frequency', fontsize=12)
axes[0].set_title('Distribution of Sepal Length', fontsize=14, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3)

# Histogram for Petal Length
axes[1].hist(iris_df['petal_length'], bins=20, color='lightcoral', edgecolor='black')
axes[1].set_xlabel('Petal Length (cm)', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].set_title('Distribution of Petal Length', fontsize=14, fontweight='bold')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# ===========================
# 6. Bar Chart for Species Distribution
# ===========================
plt.figure(figsize=(8, 6))
species_counts.plot(kind='bar', color=['#FF6B6B', '#4ECDC4', '#45B7D1'], 
                    edgecolor='black', width=0.7)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Number of Samples', fontsize=12)
plt.title('Distribution of Species in Iris Dataset', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()