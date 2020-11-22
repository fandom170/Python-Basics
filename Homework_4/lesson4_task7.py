"""Lesson 3 task 7"""
import math

factorial_for = 5
# classic way
def fact(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n * fact(n - 1)


# yield way
def y_fact(n):
    a = 1
    if n < 0:
        yield 0
    elif n == 0:
        yield 1
    elif n == 1:
        yield 1
    for i in range(1, n+1):
        a *= i
    yield a


print(math.factorial(factorial_for))
print(fact(factorial_for))

for elem in y_fact(factorial_for):
    print(elem)


# factorials of interim numbers
def a_fact(n):
    for i in range(1, n+1):
        yield fact(i)


for elem in a_fact(factorial_for):
    print(elem)
