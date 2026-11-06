import pandas as pd

source = pd.read_csv("data/source_clean.csv")
source["date"] = pd.to_datetime(source["date"])

total = source[source["source"] == "Total"]
regions = ["nr", "wr", "sr", "er", "ner"]

# Question 1: Which region generates the most power?
region_totals = total[regions].sum().sort_values(ascending=False)
print("Total generation by region (MU):")
print(region_totals)

print()
print("Share of each region (%):")
print((region_totals / region_totals.sum() * 100).round(1))

# Question 2: How has total generation changed year by year?
year = total["date"].dt.year
yearly = total.groupby(year)["all_india"].sum()
days = total.groupby(year)["date"].nunique()
per_day = (yearly / days).round(0)
growth = (per_day.pct_change() * 100).round(1)

print()
print("Days of data per year:")
print(days)

print()
print("Average generation per day (MU):")
print(per_day)

print()
print("Growth in daily average vs previous year (%):")
print(growth)

# Question 3: Which months generate the most power?
month = total["date"].dt.month
monthly = total.groupby(month)["all_india"].mean().round(0)

print()
print("Average generation per day by month (MU):")
print(monthly)