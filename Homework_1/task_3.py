"""Lesson 1 Task 3"""

# variant 1
n = input("Please enter desired number: \n")
print(int(n) + int(n + n) + int(n + n + n))

# variant 2
n = input("Please enter desired number: \n")
print(int(n) + int(n * 2) + int(n * 3))

# variant 3. For single numbers desirable
n = int(input("Please enter desired number: \n"))
print(n * 123)

# variant 4. Single line
print(123 * int(input("Please enter desired number: \n")))
