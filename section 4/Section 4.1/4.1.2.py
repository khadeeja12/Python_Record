import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 'a'],
                 [7, 8, 9],
                 [10, 11, None]])

# Convert to object type
data = data.astype(object)

def is_numeric(row):
    return all(isinstance(x, (int, float)) for x in row) and all(x is not None for x in row)

mask = np.array([is_numeric(row) for row in data])
cleaned_data = data[mask]

print(cleaned_data)
