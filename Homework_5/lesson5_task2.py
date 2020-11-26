"""Lesson 5 task 2"""

lines = 0
words = 0
with open("text_file_hw5-02.txt", "r", encoding="utf-8") as f:
    while True:
        text_line = f.readline().split()
        if not text_line:
            break
        lines += 1
        words += len(text_line)

print(f"Linked file contains {words} word(s) and {lines} line(s).")
