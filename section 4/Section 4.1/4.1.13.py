import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

inner_product = np.dot(vector_a, vector_b)
outer_product = np.outer(vector_a, vector_b)
cross_product = np.cross(vector_a, vector_b)

print("Vector A:")
print(vector_a)
print("\nVector B:")
print(vector_b)
print("\nInner Product:")
print(inner_product)
print("\nOuter Product:")
print(outer_product)
print("\nCross Product:")
print(cross_product)
