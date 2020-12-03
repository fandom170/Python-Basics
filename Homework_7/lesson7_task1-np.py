"""Lesson 7 task 1 calculations using numpy"""
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        line = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                line += f"{self.matrix[i][j]}\t"
            line += '\n'
            return line

    def __add__(self, other):
        return Matrix(np.array(self.matrix) + np.array(other.matrix))


matrix_init_1 = [[1, 2, 3], [4, 5, 6]]
matrix_init_2 = [[1, 2, 3]]

matrix_init_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix_init_4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

matrix_1 = Matrix(matrix_init_1)
matrix_2 = Matrix(matrix_init_2)

print(matrix_1)
matrix3 = (matrix_1 + matrix_2)
print(matrix3)
