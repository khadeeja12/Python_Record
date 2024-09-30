import numpy as np

covariance_matrix = np.array([[2.5, 1.0],
                               [1.0, 5.0]])

std_dev = np.sqrt(np.diag(covariance_matrix))
correlation_matrix = covariance_matrix / np.outer(std_dev, std_dev)

print("Covariance Matrix:")
print(covariance_matrix)
print("\nCorrelation Matrix:")
print(correlation_matrix)
