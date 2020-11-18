"""Lesson 3 task 1"""


def divide(a, b):
    """Function makes the division"""
    try:
        d = float(a)/float(b)
    except ZeroDivisionError:
        print("In the normal case dvision by zero is not allowed!")
        return None
    except ValueError:
        print("You have entered wrong arguments.")
        return None
    return d


x = input("Please enter first numerical argument for division: \n")
y = input("Please enter second numerical argument for division: \n")

result = divide(x, y)
print("Result of division is {}.".format(result if result or result == 0 else "not defined"))


