import pandas as pd

df = pd.DataFrame(columns=['name', 'score', 'age'])

data = {'name': 'Alice', 'score': 85, 'age': 24}

df = df._append(data, ignore_index=True)

print(df)
