import pandas as pd

series_a = pd.Series([10, 20, 30, 40])
series_b = pd.Series([1, 2, 3, 4])

addition = series_a + series_b
subtraction = series_a - series_b
multiplication = series_a * series_b
division = series_a / series_b

print("Series A:")
print(series_a)
print("\nSeries B:")
print(series_b)
print("\nAddition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nMultiplication:")
print(multiplication)
print("\nDivision:")
print(division)
