import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

first_three_rows = df.head(3)

print("Original DataFrame:")
print(df)
print("\nFirst 3 Rows of the DataFrame:")
print(first_three_rows)
