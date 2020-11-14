"""Lesson 2 task 2"""
some_list = []

while True:
    val = input("Please enter any value to add element to list. \n Enter STOP to stop entering: \n")
    if val.lower() == 'stop':
        break
    elif val is None:
        continue
    some_list.append(val)

for i in range(1, len(some_list), 2):
    some_list[i], some_list[i-1] = some_list[i - 1], some_list[i]

for elem in some_list:
    print(elem, end='')
