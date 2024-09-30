import pandas as pd

series_of_lists = pd.Series([[1, 2, 3], [4, 5], [6, 7, 8, 9]])

flattened_series = series_of_lists.explode()

print("Original Series of Lists:")
print(series_of_lists)
print("\nFlattened Series:")
print(flattened_series)
