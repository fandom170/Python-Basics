"""Lesson 2 task 1"""

# int string float byte boolean tuple dict list set etc
eat = set('food')
some_list = [1,
             1 + 6j,
             'Different types',
             162.25,
             b'line',
             False,
             ('a', 'l', 'r', 'e', 'a', 'd', 'y'),
             {1: 'e', 2: 'v', 3: 'e', 4: 'n', 5: 'i', 6: 'n', 7: 'g'},
             ['w', 'a', 'n', 't', ' ', 't', 'o'],
             eat,
             None
             , Exception]
for elem in some_list:
    print(type(elem))
