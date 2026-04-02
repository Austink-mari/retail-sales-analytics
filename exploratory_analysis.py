

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("theme_park_retail_sales.csv")
###Data Inspection###

#print("Dataset shape:", df.shape)
#df.info
#df.describe

###Converting Date Column from text to date type###

df['order_date']= pd.to_datetime(df['order_date'])
#print(df['order_date'].dtype)

###Monthly Revenue Trend###

monthly= df.groupby(df['order_date'].dt.to_period('M'))['net_revenue'].sum()
plt.figure(figsize=(12,5))
monthly.plot(kind='line', marker='o', color='#0072CE')
plt.title("Monthly Net Revenue (2024-2025)", fontsize=14)
plt.xlabel("Month")
plt.ylabel('Net Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue.png", dpi=150)
plt.show()

###Revenue By Category###

cat_revenue=df.groupby("category")['net_revenue'].sum().sort_values()
plt.figure(figsize=(8,5))
cat_revenue.plot(kind='barh', color='#0072CE')
plt.title("Total Net Revenue by Category")
plt.xlabel("Net Revenue ($)")
plt.tight_layout()
plt.savefig('revenue_by_category.png', dpi=150)
plt.show()

###Discount Impact Analysis

discount_analysis=df.groupby("discount_pct").agg(avg_satisfaction=('customer_satisfaction','mean'),
return_rate=('returned','mean'),
order_count=('order_id','count') ).round(3)
print(discount_analysis)

###Correlation Heatmap

numeric_cols=df.select_dtypes(include='number')
plt.figure(figsize=(10,7))
sns.heatmap(numeric_cols.corr(), annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()


# Revenue per channel over time (customer journey touchpoint analysis)
channel_monthly = df.groupby(
    [df["order_date"].dt.to_period("M"), "sales_channel"]
)["net_revenue"].sum().unstack()

channel_monthly.plot(kind="area", stacked=True, figsize=(12, 6),
                      colormap="Set2")
plt.title("Revenue by Channel Over Time")
plt.xlabel("Order Date (Month)")
plt.ylabel("Net Revenue ($)")
plt.tight_layout()
plt.savefig("channel_mix_over_time.png", dpi=150)
plt.show()
