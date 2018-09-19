# -*- coding: UTF-8 -*-

length = 4
matrix = []

for i in range(length):
    matrix.append([])
    for j in range(length):
        matrix[i].append(1.0/(i+j+1))
    print(matrix[i])
