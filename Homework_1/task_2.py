"""Lesson 1 Task 2"""

time_seconds = int(input("Enter time in seconds, please: \n"))

print("Entered time is {:02}:{:02}:{:02}".format(time_seconds // 3600,
                                                 (time_seconds % 3600) // 60,
                                                 (time_seconds % 3600) % 60))
