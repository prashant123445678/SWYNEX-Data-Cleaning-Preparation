import pandas as pd
import statsmodels.api as sm

# Load public Mauna Loa weekly CO2 dataset
df = sm.datasets.co2.load_pandas().data.copy()
df.index.name = "date"
df = df.reset_index()

# Correct data types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["co2"] = pd.to_numeric(df["co2"], errors="coerce")

# Remove invalid dates and exact duplicate records
df = df.dropna(subset=["date"]).sort_values("date")
df = df.drop_duplicates(subset=["date", "co2"], keep="first")

# Fill missing CO2 measurements using time interpolation
df = df.set_index("date")
df["co2"] = df["co2"].interpolate(method="time").ffill().bfill()
df = df.reset_index()

# Final types
df["date"] = pd.to_datetime(df["date"])
df["co2"] = df["co2"].astype(float)

df.to_csv("cleaned/co2_cleaned.csv", index=False)
print("Cleaned dataset saved to cleaned/co2_cleaned.csv")
print(df.info())
