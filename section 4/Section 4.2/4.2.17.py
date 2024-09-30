import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 90, 75, 88],
    'age': [24, 27, 22, 32]
}

df = pd.DataFrame(data)

# Find the row where the value of 'score' is maximum
max_row = df.loc[df['score'].idxmax()]

print("Row with the maximum 'score':")
print(max_row)
