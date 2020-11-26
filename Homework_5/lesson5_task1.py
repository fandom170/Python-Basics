"""Lesson 5 task 1"""

with open("text_file_hw5-01.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("Please enter new line for file: \n")
        if not line:
            break
        f.write(line + "\n")
