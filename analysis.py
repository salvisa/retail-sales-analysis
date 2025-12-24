import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load cleaned data
print("Loading cleaned dataset...")
df = pd.read_csv('train_cleaned.csv')

# Convert dates back to datetime (they're saved as strings in CSV)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print("="*70)
print("RETAIL SALES ANALYSIS")
print("="*70)

# ==========================================
# BUSINESS QUESTION 1: What are our top-selling categories?
# ==========================================
print("\n1. TOP-SELLING CATEGORIES BY REVENUE")
print("-" * 50)

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(category_sales)
print(f"\nTotal Revenue: ${df['Sales'].sum():,.2f}")

# Visualization
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color=['#2E86AB', '#A23B72', '#F18F01'])
plt.title('Total Sales by Category', fontsize=16, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('category_sales.png', dpi=300, bbox_inches='tight')
print("✓ Saved: category_sales.png")

# ==========================================
# BUSINESS QUESTION 2: Which regions generate the most revenue?
# ==========================================
print("\n2. REGIONAL PERFORMANCE")
print("-" * 50)

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

# Visualization
plt.figure(figsize=(10, 6))
region_sales.plot(kind='bar', color=['#06A77D', '#D4AF37', '#C73E1D', '#4A5899'])
plt.title('Total Sales by Region', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('region_sales.png', dpi=300, bbox_inches='tight')
print("✓ Saved: region_sales.png")

# ==========================================
# BUSINESS QUESTION 3: What's our sales trend over time?
# ==========================================
print("\n3. SALES TRENDS OVER TIME")
print("-" * 50)

# Create year-month column
df['Year-Month'] = df['Order Date'].dt.to_period('M')

# Monthly sales
monthly_sales = df.groupby('Year-Month')['Sales'].sum()
print(f"Average Monthly Sales: ${monthly_sales.mean():,.2f}")
print(f"Highest Month: {monthly_sales.idxmax()} (${monthly_sales.max():,.2f})")
print(f"Lowest Month: {monthly_sales.idxmin()} (${monthly_sales.min():,.2f})")

# Visualization
plt.figure(figsize=(14, 6))
monthly_sales.plot(kind='line', marker='o', linewidth=2, markersize=4, color='#2E86AB')
plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sales_trend.png', dpi=300, bbox_inches='tight')
print("✓ Saved: sales_trend.png")

# ==========================================
# BUSINESS QUESTION 4: Which customer segments are most valuable?
# ==========================================
print("\n4. CUSTOMER SEGMENT ANALYSIS")
print("-" * 50)

segment_sales = df.groupby('Segment')['Sales'].agg(['sum', 'mean', 'count'])
segment_sales.columns = ['Total Sales', 'Average Order Value', 'Number of Orders']
print(segment_sales)

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Total sales by segment
segment_sales['Total Sales'].plot(kind='bar', ax=ax1, color=['#06A77D', '#F18F01', '#C73E1D'])
ax1.set_title('Total Sales by Customer Segment', fontsize=14, fontweight='bold')
ax1.set_xlabel('Segment', fontsize=11)
ax1.set_ylabel('Total Sales ($)', fontsize=11)
ax1.tick_params(axis='x', rotation=45)

# Average order value by segment
segment_sales['Average Order Value'].plot(kind='bar', ax=ax2, color=['#2E86AB', '#A23B72', '#D4AF37'])
ax2.set_title('Average Order Value by Segment', fontsize=14, fontweight='bold')
ax2.set_xlabel('Segment', fontsize=11)
ax2.set_ylabel('Average Order Value ($)', fontsize=11)
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('segment_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: segment_analysis.png")

# ==========================================
# BUSINESS QUESTION 5: What are our top 10 products?
# ==========================================
print("\n5. TOP 10 PRODUCTS BY REVENUE")
print("-" * 50)

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

# Visualization
plt.figure(figsize=(12, 8))
top_products.plot(kind='barh', color='#2E86AB')
plt.title('Top 10 Products by Revenue', fontsize=16, fontweight='bold')
plt.xlabel('Sales ($)', fontsize=12)
plt.ylabel('Product', fontsize=12)
plt.tight_layout()
plt.savefig('top_products.png', dpi=300, bbox_inches='tight')
print("✓ Saved: top_products.png")

# ==========================================
# SUMMARY INSIGHTS
# ==========================================
print("\n" + "="*70)
print("KEY INSIGHTS SUMMARY")
print("="*70)

print(f"""
1. REVENUE OVERVIEW:
   - Total Revenue: ${df['Sales'].sum():,.2f}
   - Total Orders: {len(df):,}
   - Average Order Value: ${df['Sales'].mean():,.2f}

2. TOP PERFORMERS:
   - Best Category: {category_sales.idxmax()} (${category_sales.max():,.2f})
   - Best Region: {region_sales.idxmax()} (${region_sales.max():,.2f})
   - Best Customer Segment: {segment_sales['Total Sales'].idxmax()}

3. TIME ANALYSIS:
   - Date Range: {df['Order Date'].min().date()} to {df['Order Date'].max().date()}
   - Peak Month: {monthly_sales.idxmax()}
   
4. SHIPPING:
   - Most Common Ship Mode: {df['Ship Mode'].mode()[0]}
""")

print("\n✓ Analysis complete! All visualizations saved.")
print("\nNext steps:")
print("1. Review the generated PNG files")
print("2. Create a Tableau dashboard using train_cleaned.csv")
print("3. Update your README with findings")