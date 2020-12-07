"""Lesson 8 task 7"""


class ComplexNumber:
    def __init__(self, *args):
        try:
            self.real = args[0]
        except (TypeError, IndexError):
            self.real = 0
        try:
            self.img = args[1]
        except (TypeError, IndexError):
            self.img = 0

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __str__(self):
        return f"({self.real}+{self.img}j)" if self.img >= 0 else f"({self.real}{self.img}j)"

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.img * other.img,
                             self.real * other.img + self.img * other.real)

    def set_number_from_str(self, number):
        try:
            numbers = number.split('+')
            self.real = int(numbers[0])
            self.img = int(numbers[1][:-1])
        except ValueError:
            print("Entered number are not complex number which should be in 'a+bj' format")


cmplx = ComplexNumber(1, 1)
print(cmplx)
cmplx.set_number_from_str('2+3j')
cmplx2 = ComplexNumber(-1, 1)
print(f"Summ is {cmplx + cmplx2}")
print(f"Multiplication result: {cmplx * cmplx2}")

a = complex(2, 3)
b = complex(-1, 1)
print(f"Result of sum for python lib: {a+b}")
print(f"Result of multiplication for python lib: {a*b}")

cmplx3 = ComplexNumber()
print(cmplx3)
