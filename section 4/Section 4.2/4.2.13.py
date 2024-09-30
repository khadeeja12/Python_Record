import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 90, 75, 88],
    'age': [24, 27, 22, 32]
}

df = pd.DataFrame(data)

new_row = pd.DataFrame({'name': ['Eva'], 'score': [95], 'age': [29]})

df = pd.concat([df, new_row], ignore_index=True)

print("DataFrame after adding a new row:")
print(df)
