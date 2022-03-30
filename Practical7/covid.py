# First do the imports.
import numpy
import pandas as pd
import matplotlib.pyplot as plt
# Create the dataframe.
covid_data = pd.read_csv("full_data.csv")
# Show the first and third columns from rows 10-20 (inclusive).
print(covid_data.iloc[10:21, [1,3]])
# Use a Boolean to show “total cases” for all rows corresponding to Afghanistan.
a = covid_data.loc[:, "location"] == "Afghanistan"
print(covid_data.loc[a, "total_cases"])
# Create objects to save different columns.
china_date = covid_data.loc[covid_data.loc[:, "location"] == "China", "date"]
china_new_cases = covid_data.loc[covid_data.loc[:, "location"] == "China", "new_cases"]
china_new_deaths = covid_data.loc[covid_data.loc[:, "location"] == "China", "new_deaths"]
# Compute the means of new cases and new deaths in China.
print(numpy.mean(china_new_cases))
print(numpy.mean(china_new_deaths))
# There was only a small proportion of infected people get killed.
# Make boxplot and plot.
plt.boxplot(china_new_cases)
plt.show()
plt.boxplot(china_new_deaths)
plt.show()
# Answer the question in question.txt.
plt.plot(china_date, china_new_cases, 'c+')
# Add the x-label every 5 dates and rotate it.
plt.xticks(china_date.iloc[0:len(china_date):5], rotation=-90)
plt.show()
plt.plot(china_date, china_new_deaths, 'r+')
plt.xticks(china_date.iloc[0:len(china_date):5], rotation=-90)
plt.show()
