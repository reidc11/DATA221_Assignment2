# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 6
# In this question, you will create a simple category based on crime levels and compare unemployment rates between the groups.
# Using crime.csv:
#   • Load the dataset into a pandas DataFrame.
#   • Create a new column called risk based on ViolentCrimesPerPop:
#        – If ViolentCrimesPerPop is greater than or equal to 0.50, set risk = "High-Crime".
#       – Otherwise, set risk = "LowCrime".
#   • Group the data by the risk column.
#   • For each group, calculate the average value of PctUnemployed.
#   • Print the average unemployment rate for both HighCrime and LowCrime groups in a clear format.

import pandas as pd

crime_dataframe = pd.read_csv('crime.csv')
crime_dataframe['risk'] = ""

for i in range(len(crime_dataframe)):
    risk_level = crime_dataframe.loc[i, 'ViolentCrimesPerPop']

    if risk_level >= 0.5:
        crime_dataframe.loc[i, 'risk'] = 'High-Crime'
    else:
        crime_dataframe.loc[i, 'risk'] = 'Low-Crime'

average_unemployed = crime_dataframe.groupby('risk')['PctUnemployed'].mean()

print('Average Unemployment by Crime Level')
print(f"High-Crime: {average_unemployed['High-Crime'] * 100:.2f}%")
print(f"Low-Crime: {average_unemployed['Low-Crime'] * 100:.2f}%")
