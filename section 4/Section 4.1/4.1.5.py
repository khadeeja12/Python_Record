import numpy as np

array_3d = np.array([[[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]],

                      [[10, 11, 12],
                       [13, 14, 15],
                       [16, 17, 18]]])

diagonals = []
for i in range(array_3d.shape[0]):
    diagonals.append(np.diagonal(array_3d[i]))

print(diagonals)
