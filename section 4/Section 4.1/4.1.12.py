import numpy as np


matrix_a = np.array([[1 + 2j, 2 + 3j],
                     [3 + 4j, 4 + 5j]])

matrix_b = np.array([[5 + 6j, 6 + 7j],
                     [7 + 8j, 8 + 9j]])


result = np.dot(matrix_a, matrix_b)

print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("\nResult of Matrix Multiplication:")
print(result)
