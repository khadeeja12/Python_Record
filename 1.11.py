# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Set Union
union_result = set1.union(set2)
print(f"Union of Set1 and Set2: {union_result}")

# 2. Set Intersection
intersection_result = set1.intersection(set2)
print(f"Intersection of Set1 and Set2: {intersection_result}")

# 3. Set Difference (set1 - set2)
difference_result = set1.difference(set2)
print(f"Difference of Set1 and Set2 (Set1 - Set2): {difference_result}")

# 3. Set Difference (set2 - set1)
difference_result_reverse = set2.difference(set1)
print(f"Difference of Set2 and Set1 (Set2 - Set1): {difference_result_reverse}")
