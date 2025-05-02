import pandas as pd
import numpy as np
import os

life_df = pd.read_csv("life expectancy.csv", skiprows=4)
health_df = pd.read_csv("health_exp.csv", skiprows=4)

life_df = life_df.drop(columns=["Indicator Name", "Indicator Code"])
health_df = health_df.drop(columns=["Indicator Name", "Indicator Code"])

life_df = life_df.melt(id_vars=["Country Name", "Country Code"], var_name="Year", value_name="LifeExpectancy")
health_df = health_df.melt(id_vars=["Country Name", "Country Code"], var_name="Year", value_name="HealthSpending")

life_df = life_df[life_df["Year"].str.isnumeric()]
health_df = health_df[health_df["Year"].str.isnumeric()]

life_df["Year"] = life_df["Year"].astype(int)
health_df["Year"] = health_df["Year"].astype(int)

merged_df = pd.merge(life_df, health_df, on=["Country Name", "Country Code", "Year"])
merged_df = merged_df.dropna()

os.makedirs("data", exist_ok=True)
merged_df.to_csv("data/merged_data.csv", index=False)

print(merged_df.head(10))