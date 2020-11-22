"""Lesson 4 task 1"""

from sys import argv

try:
    hours = float(argv[1])
    overtime_hours = float(argv[3])
    pay_rate = float(argv[2])
    overtime_rate = float(argv[4])

    print("For entered {} hours of work with {} unit per work hour your total month rate is {}\n"
          "overtime work was {} hours and {} units per hour.\n"
          "Total is {}".format(hours, pay_rate, hours * pay_rate, overtime_hours,
                               overtime_rate, hours * pay_rate + overtime_rate * overtime_hours))
except ValueError:
    print("One of the arguments entered had incorrect format.")
except TypeError:
    print("One of the arguments entered had incorrect format.")
except IndexError:
    print("Make sure, please that you entered correct quantity of arguments")
except NameError:
    print("Make sure, please that you entered correct quantity of arguments")




