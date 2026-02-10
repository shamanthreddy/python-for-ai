import os
import pandas as pd
import json

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

df = pd.read_csv(data_path)
print("CSV data")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# calculate totol and add
df['total'] = df['quantity'] * df['price']
print("\n with total")
print(df)

os.makedirs('output', exist_ok=True)

# Save different formats
#1 JSON
df.to_json('output/sales_data.json', orient='records', indent=2)

# Excel
df.to_excel('output/sales_data.xlsx', index=False)

# Updated CSV
df.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")