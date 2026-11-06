import pandas as pd
from sklearn.linear_model import LinearRegression

monthly = pd.read_csv("data/monthly.csv")

X = pd.get_dummies(monthly[["t", "month"]], columns=["month"], dtype=int)
y = monthly["avg_mu_per_day"]

train = monthly["year"] <= 2021
test = monthly["year"] >= 2022

model = LinearRegression()
model.fit(X[train], y[train])

result = monthly.loc[test, ["year", "month"]].copy()
result["actual"] = y[test].round(0)
result["predicted"] = model.predict(X[test]).round(0)
result["difference"] = result["actual"] - result["predicted"]

print(result.to_string(index=False))
print("Average difference:", round(result["difference"].mean(), 1))