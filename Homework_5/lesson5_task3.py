"""Lesson 5 task 3"""
import csv

# work with usual file
file_total = 0
count_lines = 0
less_than_twenty = []
try:
    fl = open('text_file_hw5-03.txt', 'r', encoding='utf-8')
    while True:
        employee = fl.readline().split()
        if not employee:
            break
        try:
            salary_file = float(employee[-1])
            file_total += salary_file
            if salary_file < 20000:
                less_than_twenty.append(employee[:-1])
        except ValueError:
            print(f'Value of salary for {employee[0:2]} has not been found or line has invalid format.\n'
                  f' Person will be skipped')
            continue
        except IndexError:
            print(f"Value of salary for {employee[0:2]} has not been found. \nPerson will be skipped")
        count_lines += 1
    fl.close()
    print("Average salary for all employees in organisation is {:.2f}.\nFollowing people have salary less than 20 "
          "000.00: ".format(file_total / count_lines))
    [print(name) for name in less_than_twenty]
except IOError:
    print("Something went wrong or required file has not been found.")

# work with csv
poor_people = []
total = 0
salary = None
with open('text_file_hw5-03.csv', 'r', encoding='utf-8') as f:
    file_reader = csv.reader(f, delimiter=',')
    count = 0
    title = True
    for row in file_reader:
        if title:
            # skip title
            title = False
            continue
        try:
            salary = float(row[1])
            total += salary
            if salary < 20000:
                ln, fn, mn = row[0].split()
                poor_people.append(ln)
        except ValueError:
            print(f"Value for {row[0]} has not been found. Person will be skipped")
            continue
        count += 1
    print("Average salary for all employees in organisation is {:.2f}.\nFollowing people have salary less than 20 "
          "000.00: ".format(total / count))
    [print(name) for name in poor_people]
