"""Lesson 4 Task 2"""
import random
# init_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

init_list = [random.randint(1, 50) for number in range(1, 50)]
print([init_list[number] for number in range(1, len(init_list)) if init_list[number] > init_list[number - 1]])



