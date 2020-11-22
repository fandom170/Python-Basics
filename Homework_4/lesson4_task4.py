"""Lesson 4 task 4"""
# variant with generator of random values in list
import random
init_list = [random.randint(1, 100) for number in range(1, 500)]
print([number for number in init_list if init_list.count(number) == 1])

# variant with list given
init_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([number for number in init_list if init_list.count(number) == 1])
