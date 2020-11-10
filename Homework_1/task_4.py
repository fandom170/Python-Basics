"""Lesson 1 Task 4"""

n = int(input("Please enter positive integer value: \n"))

max_d = 0
while True:
    pos_n = n % 10
    n = n // 10
    if n == 0:
        break
    if pos_n > max_d:
        max_d = pos_n
print(f"Max digit in the number is {max_d}")
