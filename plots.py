import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged_df = pd.read_csv("data/merged_data.csv")

countries = ["United States", "India", "Brazil"]
plt.figure(figsize=(10, 6))
for country in countries:
    subset = merged_df[merged_df["Country Name"] == country]
    plt.plot(subset["Year"], subset["LifeExpectancy"], label=country)
plt.xlabel("Year")
plt.ylabel("Life Expectancy (Years)")
plt.title("Life Expectancy Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("life_expectancy_trend.png")
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=merged_df, x="HealthSpending", y="LifeExpectancy", alpha=0.5)
plt.xlabel("Health Spending (USD)")
plt.ylabel("Life Expectancy (Years)")
plt.title("Health Spending vs Life Expectancy")
plt.tight_layout()
plt.savefig("spending_vs_life_expectancy.png")
plt.show()
