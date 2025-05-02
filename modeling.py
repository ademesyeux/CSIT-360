import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


merged_df = pd.read_csv("data/merged_data.csv")
merged_df = merged_df[merged_df["HealthSpending"] > 0]  # avoid log(0)
merged_df["LogHealthSpending"] = np.log1p(merged_df["HealthSpending"])

X = merged_df[["HealthSpending", "LogHealthSpending"]]
y = merged_df["LifeExpectancy"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit multiple linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Plot prediction vs actual
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Life Expectancy")
plt.ylabel("Predicted Life Expectancy")
plt.title("Actual vs Predicted Life Expectancy")
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.close()

# Residuals plot
residuals = y_test - y_pred
plt.figure(figsize=(8, 5))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs Predicted Life Expectancy")
plt.xlabel("Predicted Life Expectancy")
plt.ylabel("Residuals")
plt.tight_layout()
plt.savefig("residuals_plot.png")
plt.show()