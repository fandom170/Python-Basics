"""Lesson 3 task 5"""
from functools import reduce

total = 1

init_list = [number for number in range(100, 1000 + 1) if number % 2 == 0]


def multiply(elem1, elem2):
    return elem1 * elem2


for i in init_list:
    total *= i

print(init_list)
print(reduce(multiply, init_list))

# comparing with loop way
print(reduce(multiply, init_list) - total)
