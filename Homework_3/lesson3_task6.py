"""Lesson 3 task 6"""


# variant 1
def int_func(word):
    return word.title()


# variant 2 (English only)
def int_func_char(word):
    letter = ord(word[0])
    symbol = chr(letter) if 65 < letter < 90 else chr(letter - 32)
    return symbol + word[1:]


text_line = input().split()

for elem in text_line:
    print(int_func(elem), end=' ')

for elem in text_line:
    print(int_func_char(elem), end=' ')



