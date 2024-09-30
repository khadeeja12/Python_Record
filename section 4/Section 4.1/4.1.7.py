import numpy as np

dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'i4')]

students = np.array([
    ('Khadeeja', 5.5, 10),
    ('Faris', 6.0, 10),
    ('Sameera', 5.8, 9),
    ('Alfitha', 5.5, 9),
    ('Rasheeda', 6.1, 10)
], dtype=dtype)

sorted_students = np.sort(students, order=['class', 'height'])

print("Sorted Students:")
print(sorted_students)
