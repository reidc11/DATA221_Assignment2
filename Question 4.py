# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 4
# This question involves filtering tabular data and saving the results to a new file.
# Using student.csv:
# • Load the dataset into a DataFrame.
# • Filter students where studytime ≥ 3, internet = 1, and absences ≤ 5.
# • Save the filtered data to high_engagement.csv.
# • Print the number of students saved and their average grade

import pandas as pd

student_dataframe = pd.read_csv('student.csv')


filtered_students = student_dataframe[
    (student_dataframe['studytime'] >= 3) &
    (student_dataframe['internet'] == 1) &
    (student_dataframe['absences'] <= 5)
]
filtered_students.to_csv('high_engagement.csv', index=False)
num_students = len(filtered_students)

average_grade = filtered_students['grade'].mean()

print(f'Number of Students in filtered_students: {num_students}')
print(f'Average grade of Students in filtered_students: {average_grade}')

