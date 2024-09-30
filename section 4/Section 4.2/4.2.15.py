import pandas as pd
import numpy as np

# Initial data
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, np.nan, 75, 88],
    'age': [24, 27, np.nan, 32]
}

df = pd.DataFrame(data)

# Replace NaN values with zeros in 'score' column
df['score'].fillna(0, inplace=True)

print("DataFrame after replacing NaN values with zeros in 'score' column:")
print(df)

# Drop specified rows
rows_to_drop = [1, 3]  # Rows to drop by index
df = df.drop(rows_to_drop)

print("\nDataFrame after dropping specified rows:")
print(df)
