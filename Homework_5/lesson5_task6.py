"""Lesson 5 task 6"""
import os

file_name = 'text_file_hw5-06.txt'
file_exists = os.path.exists(file_name)
result = {}

if file_exists:
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            data_line = f.readline().split()
            if not data_line:
                break
            subject = data_line[0][:-1]
            try:
                lectures = float(data_line[1][:-3]) if data_line[1] != '-' else 0
                practise = float(data_line[2][:-4]) if data_line[2] != '-' else 0
                labs = float(data_line[3][:-5]) if data_line[3] != '-' else 0
                total_hours = lectures + practise + labs
            except ValueError:
                print(f"Units for subject {subject} were defined incorrectly.")
                continue
            if subject not in result:
                result[subject] = total_hours
            else:
                result[subject] += total_hours
else:
    print("No such file.")

print(result)


# variant 2 without slices
def detect_numeric(s):
    if s == '-':
        return None
    try:
        return float(''.join(filter(str.isdigit, s)))
    except ValueError:
        return None


total_hours = 0
result2 = {}
if file_exists:
    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            data_line = f.readline().split()
            if not data_line:
                break
            total = 0
            line_total = [total + detect_numeric(i) for i in data_line if detect_numeric(i) is not None]
            result2[data_line[0]] = sum(line_total)
else:
    print("No such file.")

print(result2)
