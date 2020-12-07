"""Lesson 8 task 4, 5, 6"""
from Homework_8.lesson8_task4_of import Copier, Scanner, Printer


class Warehouse:
    number = 0
    wh_printer = []
    wh_scanner = []
    wh_copier = []

    def __init__(self):
        tmp = Warehouse.init_data()
        for elem in tmp:
            if elem.type == 'Printer':
                self.wh_printer.append([elem, 1])
                Warehouse.number += 1
            elif elem.type == 'Scanner':
                self.wh_scanner.append([elem, 1])
                Warehouse.number += 1
            elif elem.type == 'Copier':
                self.wh_copier.append([elem, 1])
                Warehouse.number += 1

    @staticmethod
    def init_data():
        with open('init_data.txt', 'r', encoding='utf-8') as f:
            data_list = []
            counter = 0
            for line in f:
                data_line = line.split(',')
                counter += 1
                if data_line[0] == 'Printer':
                    data_list.append(Printer(*data_line[1:]))
                elif data_line[0] == 'Scanner':
                    data_list.append(Scanner(*data_line[1:]))
                elif data_line[0] == 'Copier':
                    data_list.append(Copier(*data_line[1:]))
                else:
                    print(f"No such element at line {counter}")
            return data_list

    @staticmethod
    def check_existence(item, item_list):
        for i in range(len(item_list)):
            if item_list[i][0].model == item.model:
                return i
        return -1

    @classmethod
    def add_item(cls, item, qty):
        if qty.isdecimal():
            Warehouse.number += 1
            if item.type == 'Printer':
                index = Warehouse.check_existence(item, cls.wh_printer)
                if index == -1:
                    cls.wh_printer.append([item, qty])
                else:
                    cls.wh_printer[index][1] += qty
            elif item.type == 'Scanner':
                index = Warehouse.check_existence(item, cls.wh_scanner)
                if index == -1:
                    cls.wh_scanner.append([item, qty])
                else:
                    cls.wh_scanner[index][1] += qty
            if item.type == 'Copier':
                index = Warehouse.check_existence(item, cls.wh_copier)
                print(f"index ={index}")
                if index == -1:
                    cls.wh_copier.append([item, qty])
                else:
                    print("append")
                    cls.wh_copier[index][1] += qty
        else:
            print("\033[96mQuantity is not numeric value. Item was not added.\033[0m")

    @classmethod
    def remove_item(cls, item, qty):
        if qty.isdecimal():
            if item.type == 'Printer':
                index = Warehouse.check_existence(item, cls.wh_printer)
                if index != -1 and cls.wh_printer[index][1] >= qty:
                    cls.wh_printer[index][1] -= qty
                    return cls.wh_printer[index][0]
                else:
                    print("\033[95mRequest cannot be executed. Insufficient amount in warehouse.\n"
                          f"Current amount is {cls.wh_printer[index][1]}.\033[0m")
            elif item.type == 'Scanner':
                index = Warehouse.check_existence(item, cls.wh_scanner)
                if index != -1 and cls.wh_scanner[index][1] >= qty:
                    cls.wh_scanner[index][1] -= qty
                    return cls.wh_scanner[index][0]
                else:
                    print("\033[95mRequest cannot be executed. Insufficient amount in warehouse.\n"
                          f"Current amount is {cls.wh_scanner[index][1]}.\033[0m")
            elif item.type == 'Copier':
                index = Warehouse.check_existence(item, cls.wh_copier)
                if index != -1 and cls.wh_copier[index][1] >= qty:
                    cls.wh_copier[index][1] -= qty
                    return cls.wh_copier[index][0]
                else:
                    print("\033[95mRequest cannot be executed. Insufficient amount in warehouse.\n"
                          f"Current amount is {cls.wh_copier[index][1]}.\033[0m")
            else:
                print("\033[31mNo such item in the warehouse.\033[0m")
        else:
            print("\033[96mQuantity is not numeric value. Item was not removed from warenhouse.\033[0m")

    @staticmethod
    def warehouse_info(warehouse):
        solution = input("Which type of equipment do you want to see? \n"
                         "sc - scanner, pr - printer, cp - copier.\n"
                         "Any other entering returns all available information.\n"
                         "enter 0 to skip printing. \n")
        if solution.lower() == 'sc':
            warehouse.print_category(warehouse.wh_scanner)
        elif solution.lower() == 'pr':
            warehouse.print_category(warehouse.wh_printer)
        elif solution.lower() == 'cp':
            warehouse.print_category(warehouse.wh_copier)
        elif solution == '0':
            print("Printing of warehouse content will be skipped.")
        else:
            warehouse.print_category(warehouse.wh_scanner)
            warehouse.print_category(warehouse.wh_printer)
            warehouse.print_category(warehouse.wh_copier)

    @staticmethod
    def print_category(data_list):
        for elem in data_list:
            print(f"{elem[0]} \n quantity is {elem[1]}\n")
