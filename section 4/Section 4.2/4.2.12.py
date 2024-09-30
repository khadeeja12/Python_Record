import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'score': [85, 90, 75, 88, 95],
    'age': [24, 27, 22, 32, 29]
}

df = pd.DataFrame(data)

num_rows, num_columns = df.shape

print("DataFrame:")
print(df)
print("\nNumber of Rows:", num_rows)
print("Number of Columns:", num_columns)
