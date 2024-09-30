import pandas as pd

series_a = pd.Series([1, 2, 3, 4, 5])
series_b = pd.Series([4, 5, 6, 7, 8])

not_common = pd.concat([series_a, series_b]).drop_duplicates(keep=False)

print("Series A:")
print(series_a)
print("\nSeries B:")
print(series_b)
print("\nItems not common in both Series:")
print(not_common)
