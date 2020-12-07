"""Lesson 8 task 2"""


class DivisionByZero(Exception):
    def __init__(self, text):
        self.text = text


def division(a, b):
    try:
        if b == 0:
            raise DivisionByZero("Second argument should not be zero.")
        else:
            return round(a / b, 2)
    except DivisionByZero as dz:
        print(dz)


x = float(input("Please enter numeric value: \n"))
y = float(input("Please enter divider value: \n"))

print(f"Quotient is {division(x, y)}.")
