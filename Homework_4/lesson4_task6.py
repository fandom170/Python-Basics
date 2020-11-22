"""Lesson 4 task 6"""

import random
from itertools import count, cycle


"""program is completely useless. 
It generates some sort of numerical sequence, convert it to char sequence and then prints this sequence several times.
"""


def char_convert(elem1):
    return chr(elem1 if 65 < elem1 * random.randint(1, 10) % 65 < 90 else random.randrange(65, 91))


try:
    n = int(input("Please enter length of sequence: \n"))
    iterator = count(0, 6)
    init_list = list((next(iterator) for i in range(2*n)))
    new_list = list(map(char_convert, init_list))
    iterator_cycle = cycle(new_list)
    print(list(next(iterator_cycle) for j in range(n**3)))
except ValueError:
    print("Incorrect data was entered.")
# for elem in cycle([chr(random.randint(65, 90)) for number in range(200)]):




