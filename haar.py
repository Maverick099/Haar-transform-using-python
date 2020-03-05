import math as m

import numpy as n

a = n.array([[2, 1, 2, 1], [1, 2, 3, 2], [2, 3, 4, 3], [1, 2, 3, 2]])
print(a)

x = m.sqrt(2)
h = n.array([[1, 1, 1, 1], [1, 1, -1, -1], [x, -x, 0, 0], [0, 0, x, -x]])

haar_transform_matrix = (h * (1 / 2))
print("\n", haar_transform_matrix)

haar_transform_matrix_transpose = n.transpose(haar_transform_matrix)

f = n.dot(haar_transform_matrix, a)
f = n.matrix.round(f, 4)
print("\nf=", f)

F = n.dot(f, haar_transform_matrix_transpose)
F = n.matrix.round(F, 4)
print("\nF=", F)
