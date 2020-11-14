"""Lesson 2 task 4"""

# split without specified value to split by several spaces.
text_lines = input("Please enter some words separated by spaces: \n").split()

if text_lines:
    for elem in enumerate(text_lines, 1):
        word = elem[1]
        print(f"{elem[0]}. {word[:10]}")
else:
    print("You did not enter anything.")



