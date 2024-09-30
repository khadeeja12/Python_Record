import pandas as pd
import numpy as np

random_df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])

missing_df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 1, 2, 3, 4],
    'C': [1, 2, 3, 4, 5]
})

dates_df = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Value': [10, 20, 30, 40, 50]
})

mixed_df = pd.DataFrame({
    'A': [1, 'two', 3.0, np.nan, 5],
    'B': ['apple', 2, 'banana', 'cherry', np.nan],
    'C': [True, False, True, False, True]
})

print("DataFrame with random values:")
print(random_df)

print("\nDataFrame with missing values:")
print(missing_df)

print("\nDataFrame with datetime values:")
print(dates_df)

print("\nDataFrame with mixed values:")
print(mixed_df)
