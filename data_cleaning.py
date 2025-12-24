import pandas as pd
import numpy as np

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('train.csv')

print(f"Original dataset shape: {df.shape}")
print("\n" + "="*50)

# 1. Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 2. Check data types
print("\nData types:")
print(df.dtypes)

# 3. Convert date columns to datetime with specific format
print("\nConverting date columns...")
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

# 4. Handle Postal Code (convert to integer, fill missing with 0)
print("\nCleaning Postal Code column...")
df['Postal Code'] = df['Postal Code'].fillna(0).astype(int)

# 5. Check for duplicates
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

if duplicates > 0:
    df = df.drop_duplicates()
    print(f"Removed {duplicates} duplicate rows")

# 6. Basic statistics
print("\n" + "="*50)
print("\nDataset Summary Statistics:")
print(df.describe())

# 7. Check unique values in categorical columns
print("\n" + "="*50)
print("\nUnique values in key columns:")
print(f"Ship Mode: {df['Ship Mode'].unique()}")
print(f"Segment: {df['Segment'].unique()}")
print(f"Region: {df['Region'].unique()}")
print(f"Category: {df['Category'].unique()}")

# 8. Save cleaned dataset
print("\n" + "="*50)
print("\nSaving cleaned dataset...")
df.to_csv('train_cleaned.csv', index=False)

print(f"\n✓ Cleaned dataset saved as 'train_cleaned.csv'")
print(f"✓ Final dataset shape: {df.shape}")
print("\nData cleaning complete!")