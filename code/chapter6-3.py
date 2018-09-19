# -*- coding: UTF-8 -*-

length = 5
matrix = []

for i in range(length):
    matrix.append([])
    for j in range(length):
        matrix[i].append(1 if i == j else 0)

print(matrix)
