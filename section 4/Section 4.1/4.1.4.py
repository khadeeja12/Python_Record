import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
values_to_check = [2, 4, 7]
presence = np.isin(values_to_check, array)

print(presence)
