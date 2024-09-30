import pandas as pd

series = pd.Series([10, 20, 15, 30, 25, 5, 40])

subset = series[series > 15]

print("Original Series:")
print(series)
print("\nSubset of Series (values greater than 15):")
print(subset)
