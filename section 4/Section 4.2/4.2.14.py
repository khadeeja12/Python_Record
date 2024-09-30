import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [85, 90, 75, 88],
    'age': [24, 27, 22, 32]
}

df = pd.DataFrame(data)

df.to_csv('output.csv', sep='\t', index=False)

print("DataFrame written to 'output.csv' with tab separator.")
