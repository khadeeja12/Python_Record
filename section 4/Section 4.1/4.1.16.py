import numpy as np

nums = np.array([1, 2, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6])
bins = np.array([0, 2, 4, 6])

histogram, bin_edges = np.histogram(nums, bins=bins)

print("Numbers:")
print(nums)
print("\nBins:")
print(bins)
print("\nHistogram:")
print(histogram)
print("\nBin Edges:")
print(bin_edges)
