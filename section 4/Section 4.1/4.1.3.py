import numpy as np


array = np.array([[[1]], [[2]], [[3]], [[4]]])

squeezed_array = np.squeeze(array)

print(squeezed_array)
print("New shape:", squeezed_array.shape)

