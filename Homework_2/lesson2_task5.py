"""Lesson 2 task 5"""

init_list = [7, 5, 3, 3, 2]

while True:
    new_elem = input('Please enter new element of score or enter "Stop": \n')
    if new_elem.lower() == 'stop':
        break
    if not new_elem.isdigit():
        print("Wrong element was entered.")
        continue
    new_elem = int(new_elem)
    n = init_list.count(new_elem)

    if n == 0:
        for i in range(len(init_list)):
            if new_elem > init_list[i]:
                init_list.insert(i, new_elem)
                break
        else:
            init_list.append(new_elem)
            print('append')
    else:
        elem_index = init_list.index(new_elem)
        init_list.insert(elem_index + n, new_elem)

print(init_list)

