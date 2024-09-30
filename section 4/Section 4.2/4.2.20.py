import pandas as pd

data = {
    'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'],
    'Age': [18, 22, 40, 50, 80]
}

df = pd.DataFrame(data)

bins = [0, 18, 35, 50, 100]
labels = ['Young', 'Adult', 'Middle-aged', 'Senior']

df['Age_Category'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

print(df)
