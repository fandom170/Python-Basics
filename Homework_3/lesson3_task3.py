"""Lesson 3 task 3"""


# variant 1
def my_func_list(args):
    """Function uses 'max' method of list"""
    return args.pop(args.index(max(args))) + args.pop(args.index(max(args)))


# variant 2
def my_func_list2(a, b, c):
    """Function uses sorting of array"""
    args = sorted([a, b, c])
    return args[-1] + args[-2]


"""General block"""


def enter_data(word):
    """Verify data entered"""
    try:
        number = float(word)
        return number
    except ValueError:
        print("Wrong argument was entered. Please try again")


arguments = []
while len(arguments) < 3:
    arg = enter_data(input(f"Please enter {len(arguments) + 1} argument for comparing: \n"))
    if arg or arg == 0:
        arguments.append(arg)
    else:
        continue

args1 = arguments.copy()
x = args1[0]
y = args1[1]
z = args1[2]

"""Functions execution"""
# variant 1
print(my_func_list(arguments))
# variant 2
print(my_func_list2(x, y, z))
# variant 4
# """useless Lambda"""
# sorted(args1)
# print((lambda args: args[-2] + args[-1])(args1))


