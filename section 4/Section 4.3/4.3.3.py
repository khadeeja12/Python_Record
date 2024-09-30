import pandas as pd

data = {
    'Id': [1, 2, 1, 1, 2, 1, 2],
    'type': [10, 15, 11, 20, 21, 12, 14],
    'book': ['Math', 'English', 'Physics', 'Math', 'English', 'Physics', 'English']
}

df = pd.DataFrame(data)

grouped = df.groupby(['Id', 'type', 'book']).size().reset_index(name='count')

print("Group by value counts:")
print(grouped)
