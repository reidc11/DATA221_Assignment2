# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 5
# Here you will create a new categorical variable and generate a grouped summary table.
# Using student.csv:
# • Create a new column grade_band:
#   – Low: grade ≤ 9
#   – Medium: grade 10–14
#    – High: grade ≥ 15
# • Create a grouped summary table showing for each band:
#   – number of students
#   – average absences
#    – percentage of students with internet access
# • Save the table as student_bands.csv

import pandas as pd

student_dataframe = pd.read_csv('student.csv')
student_dataframe['grade_band'] = ''


for i in range(len(student_dataframe)):
    grade = student_dataframe.loc[i, 'grade']

    if grade <= 9:
        student_dataframe.loc [i, 'grade_band'] = 'Low'
    elif grade <= 14:
        student_dataframe.loc[i, 'grade_band'] = 'Medium'
    else:
        student_dataframe.loc[i, 'grade_band'] = 'High'

#create new summary table by grade band
summary_table = (
    student_dataframe
        .groupby('grade_band')
        .agg(
            number_students=('grade', 'count'),
            average_absences=('absences', 'mean'),
            percent_internet=('internet', 'mean')
        )
)

# Convert internet proportion to percentage
summary_table['percent_internet'] = summary_table['percent_internet'] * 100

# Round data to two decimal points
summary_table = summary_table.round(2)

# Save to CSV
summary_table.to_csv('summary_table_by_band.csv', index=True)

print(summary_table)

