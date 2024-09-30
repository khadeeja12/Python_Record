import numpy as np

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

diagonal_sum = np.trace(array)

print("Original Array:")
print(array)
print("\nSum of the diagonal elements:")
print(diagonal_sum)
