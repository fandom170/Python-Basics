"""Lesson 5 task 7"""
import json
import os

filename = 'text_file_hw5-07.txt'
json_name = 'text_file_hw5-07.json'
result_list = []

with open(filename, 'r', encoding='utf-8') as f:
    total_diff = 0
    companies = {}
    count = 0
    while True:
        dataline = f.readline().split()
        if not dataline:
            break
        try:
            diff = float(dataline[2]) - float(dataline[3])
            companies[dataline[0]] = diff
            if diff > 0:
                total_diff += diff
                count += 1
        except ValueError:
            print(f"Incorrect data in file. Company {dataline[0]} skipped.")
        except IndexError:
            print("Line does not contain full information.")
    result_list.append(companies)
    result_list.append({"average": (total_diff / count)})

if os.path.exists(json_name):
    os.remove(json_name)

with open(json_name, 'w', encoding='utf-8') as fj:
    json.dump(result_list, fj, indent=4, ensure_ascii=False)
