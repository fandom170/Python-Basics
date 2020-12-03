"""Lesson 7 task 3"""


class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        """Adding cell numbers for both classes"""
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if other.cell_number > self.cell_number:
            print("Second parameter exceeds first. Subtract is impossible. Zero will be returned.")
            return Cell(0)
        else:
            return Cell(self.cell_number - other.cell_number)

    def __mul__(self, other):
        """Multiplying number of cells"""
        return Cell(self.cell_number * other.cell_number)

    def __floordiv__(self, other):
        """Division by numbers of cells"""
        return Cell(self.cell_number // other.cell_number)

    def __str__(self):
        return f"Current number of cells is {self.cell_number}"

    def make_order(self, row):
        """printing cell structure based on counter"""
        print((('*' * row + '\n') * (self.cell_number // row)) + ('*' * (self.cell_number % row)))

    @staticmethod
    def make_order_with_cell(cell, row):
        """printing cell structure based on counter - method is static and can be converted to function"""
        print((('*' * row + '\n') * (cell.cell_number // row)) + ('*' * (cell.cell_number % row)))


cluster_1 = Cell(21)
cluster_2 = Cell(7)

cluster_1 = (cluster_1 + cluster_2)
print(cluster_1 + cluster_2)
print(cluster_1 - cluster_2)
print(cluster_2 - cluster_1)
print(cluster_1 * cluster_2)
print(cluster_1 // cluster_2)

cluster_1.make_order(6)
print("")
cluster_1.make_order_with_cell(cluster_2, 3)
