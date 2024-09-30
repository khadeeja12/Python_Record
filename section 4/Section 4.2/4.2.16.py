import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 90, 75, 88],
    'age': [24, 27, 22, 32]
}

df = pd.DataFrame(data)

# Shuffle the rows of the DataFrame
shuffled_df = df.sample(frac=1).reset_index(drop=True)

print("Shuffled DataFrame:")
print(shuffled_df)
