import pandas as pd

series = pd.Series(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])

frequency_counts = series.value_counts()

print("Original Series:")
print(series)
print("\nFrequency Counts of Each Unique Value:")
print(frequency_counts)
