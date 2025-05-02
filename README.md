# Objectives
For my project, I looked at how health spending relates to life expectancy using World Bank data.

The plots in this project help visualize the connection between health spending and life expectancy. I used data from the World Bank on life expectancy at birth and current health expenditure per capita. After cleaning and merging the datasets by country and year, I focused on two main variables: how much a country spends on healthcare per person (HealthSpending) and how long people are expected to live (LifeExpectancy).

To explore this relationship, I created two plots. The first shows how life expectancy has changed over time in three countries: the United States, India, and Brazil. It helps highlight how different countries progress in different ways depending on their resources and policies. The second plot is a scatterplot showing all countries, with life expectancy on the y-axis and health spending on the x-axis. The trend shows that countries that spend more generally have higher life expectancy, though the benefit seems to level off after a certain point.

For modeling, I used multiple linear regression with both raw and log-transformed health spending as predictors. This allowed me to capture the more complex relationship between money and health outcomes. The model achieved an R-squared of 0.681 and a mean squared error of 23.24, showing a fairly strong relationship between the two variables, but also hinting that other factors beyond spending like education, infrastructure, and public health policy—matter too.
