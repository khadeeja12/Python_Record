import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 90, 75, 88],
    'age': [24, 27, 22, 32]
}

df = pd.DataFrame(data)


column_name = 'score'


if column_name in df.columns:
    print(f"Column '{column_name}' is present in the DataFrame.")
else:
    print(f"Column '{column_name}' is not present in the DataFrame.")
