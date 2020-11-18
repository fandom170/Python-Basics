"""Lesson 3 task 5"""


# variant 1
def convert(element):
    """Hust catch errors during conversion"""
    try:
        return float(element)
    except ValueError:
        print(f"incorrect symbol {element} was entered. If you want to terminate program enter 'Q', please.")
        return 0


def main_loop():
    total = 0
    stop = False
    while not stop:
        a = input().split()
        tmp_total = 0
        for elem in a:
            if elem.lower() == 'q':
                stop = True
                break
            elem = convert(elem)
            total += elem
            tmp_total += elem
        print(f"current total amount is {total}. \nCurrent entered amount is {tmp_total}.")
    print(f"General total is {total}")


main_loop()



