"""Lesson 7 task 1. Standard calculation"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_size_ext = len(list(matrix))
        self.matrix_size_int = len(list(matrix[0]))

    def __str__(self):
        line = ''
        for i in range(self.matrix_size_ext):
            for j in range(self.matrix_size_int):
                line += f"{self.matrix[i][j]}\t"
            line += '\n'
        return line

    def __getitem__(self, *args):
        self.my_list = []
        for elem in args:
            self.my_list.append(Matrix(elem))

    def get_result_matrix_shape(self, size_1, size_2):
        x1, y1 = size_1
        x2, y2 = size_2
        x = x1 if x1 > x2 else x2
        y = y1 if y1 > y2 else y2
        return x, y

    def __add__(self, other):
        size_self = self.matrix_size_ext, self.matrix_size_int
        size_other = other.matrix_size_ext, other.matrix_size_int
        if size_self != size_other:
            x, y = self.get_result_matrix_shape(size_self, size_other)
            print("Size of matrices were different. Both Matrices were converted to same size")
        else:
            x = self.matrix_size_ext
            y = self.matrix_size_int
        result = [[0 for _ in range(y)] for _ in range(x)]
        for i in range(self.matrix_size_ext):
            for j in range(self.matrix_size_int):
                result[i][j] += self.matrix[i][j]
        for i in range(other.matrix_size_ext):
            for j in range(other.matrix_size_int):
                result[i][j] += other.matrix[i][j]
        return Matrix(result)


matrix_init_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix_init_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_1 = Matrix(matrix_init_1)
matrix_2 = Matrix(matrix_init_2)

print(matrix_1)
print(matrix_2)

print(matrix_1 + matrix_2)
