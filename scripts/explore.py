import pandas as pd

files = ["data/power_source.csv", "data/power_states.csv"]

for name in files:
    df = pd.read_csv(name)
    print("=====", name, "=====")
    print("Shape:", df.shape)
    print()
    print("Data types:")
    print(df.dtypes)
    print()
    print("Missing values:")
    print(df.isnull().sum())
    print()