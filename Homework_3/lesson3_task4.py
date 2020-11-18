"""Lesson 3 task 4"""


def my_func(a, b):
    return a**b


def my_func_loop(a, b):
    y = 1/a
    if b == 0:
        return 1.0
    for i in range(abs(b)-1):
        y *= 1/a
    return y


def data_entering():
    while True:
        try:
            x = float(input("Please enter base (grater than zero): \n"))
            y = int(input("Please enter exponent value (less than zero): \n"))
        except ValueError:
            print("Wrong value(s) has been entered.")
            continue
        if x <= 0 or y > 0:
            print("Conditions for arguments were broken. Please repeat entering")
            continue
        return x, y


arr = data_entering()
print(my_func(arr[0], arr[1]))
print(my_func_loop(arr[0], arr[1]))

