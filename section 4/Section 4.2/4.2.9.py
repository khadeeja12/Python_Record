import pandas as pd

series = pd.Series([10, 20, 5, 40, 5, 30])

min_index = series.idxmin()
max_index = series.idxmax()

print("Original Series:")
print(series)
print("\nIndex of the first occurrence of the smallest value:", min_index)
print("Index of the first occurrence of the largest value:", max_index)
