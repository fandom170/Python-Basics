"""Lesson 8 task 3"""


class NotNumber(Exception):
    def __init__(self, text):
        self.text = text


numbers_list = []


def float_check(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def data_entering():
    while True:
        number = input('Please enter a number to add it to list. \n Enter "stop" or "s" to finish adding of data.\n')
        if number == 'stop' or number == 's':
            break
        try:
            if number.isdigit() or float_check(number):
                number = float(number)
                numbers_list.append(number)
            else:
                raise NotNumber("Argument sent is not numeric.")
        except NotNumber as nn:
            print(nn)
        except ValueError:
            print("entered value cannot be converted to number.")


data_entering()
print(numbers_list)
