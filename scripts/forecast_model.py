import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

monthly = pd.read_csv("data/monthly.csv")

X = pd.get_dummies(monthly[["t", "month"]], columns=["month"], dtype=int)
y = monthly["avg_mu_per_day"]

train = monthly["year"] <= 2021
test = monthly["year"] >= 2022

model = LinearRegression()
model.fit(X[train], y[train])

pred = model.predict(X[test])

mae = mean_absolute_error(y[test], pred)
percent = mae / y[test].mean() * 100

print("Train rows:", train.sum())
print("Test rows:", test.sum())
print("Average error (MU per day):", round(mae, 1))
print("Average error (percent):", round(percent, 1))