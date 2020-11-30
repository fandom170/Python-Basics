"""Lesson 6 task 2 main file"""
from Homework_6.lesson6_task2 import Road


# from lesson6_task2 import Road


def data_entering():
    width = float(input("Please enter expected road width (mm): \n"))
    length = float(input("Please enter expected road length (km): \n"))
    other = bool(input("Do you want to enter other parameters? If 'no', just press enter, any other value if 'yes'\n"))
    if other:
        layer = float(input("Please enter expected asphalt thickness (cm): \n"))
        kind = input("Please enter expected type of asphalt: 'normal', 'mold', 'pressed', 'concrete'.\n"
                     " 'normal' is set by default.\n")
    else:
        layer = 5
        kind = 'normal'
    return width, length, layer, kind


main_road = Road(*data_entering())
main_road.print_data()
