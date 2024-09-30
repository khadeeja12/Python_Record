import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'score': [85, 90, 75, 88, 95],
    'age': [24, 27, 22, 32, 29]
}

df = pd.DataFrame(data)

selected_columns = df[['name', 'score']]

print("Original DataFrame:")
print(df)
print("\nSelected 'name' and 'score' Columns:")
print(selected_columns)
