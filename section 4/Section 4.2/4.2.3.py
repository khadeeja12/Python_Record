import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)
first_column_series = df.iloc[:, 0]

print("DataFrame:")
print(df)
print("\nFirst Column as Series:")
print(first_column_series)
