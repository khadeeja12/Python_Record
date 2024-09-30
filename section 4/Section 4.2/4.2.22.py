import pandas as pd

student_data1 = {
    'student_id': ['s1', 's2', 's3', 's4', 's5'],
    'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
    'marks': [200, 210, 190, 222, 199]
}

student_data2 = {
    'student_id': ['s4', 's5', 's6', 's7', 's8'],
    'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
    'marks': [201, 200, 198, 219, 201]
}

df1 = pd.DataFrame(student_data1)
df2 = pd.DataFrame(student_data2)

combined_df = pd.concat([df1, df2], ignore_index=True)

print("Combined DataFrame:")
print(combined_df)
