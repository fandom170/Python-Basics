"""Lesson 8 task 4. Office equipment related classes."""
from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, model, weight, size):
        self.model = model
        self.weight = weight
        self.size = size

    @staticmethod
    def data_validation(data):
        try:
            return int(data)
        except ValueError:
            return 0

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def set_item(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, model, weight, size, print_type, paper_format, connection_interface):
        super().__init__(model, weight, size)
        self.type = self.__class__.__name__
        self.print_type = print_type
        self.paper_format = paper_format
        self.connection_interface = connection_interface

    @classmethod
    def set_item(cls):
        cls.model = input(f"Please enter model of Printer:\n")
        cls.weight = cls.data_validation(input(f"Please enter weight or zero if unknown: \n"))
        cls.size = cls.data_validation(input(f"Please enter max size or zero if unknown: \n"))
        cls.print_type = input(f"Please enter print type:\n")
        cls.paper_format = input(f"Please enter available paper format: \n")
        cls.connection_interface = input(f"Please enter connection interface: \n")
        print("Printer data has been entered")
        return Printer(cls.model, cls.weight, cls.size, cls.print_type, cls.paper_format, cls.connection_interface)

    def __str__(self):
        return f'Current office equipment type is {self.type}.\n' \
               f'Parameters are: \n' \
               f'model name is {self.model}\n' \
               f'weight is {self.weight}\n' \
               f'size is {self.size}\n' \
               f'print type is {self.print_type}\n' \
               f'paper format is {self.paper_format}\n' \
               f'connection interface is {self.connection_interface}.'


class Scanner(OfficeEquipment):
    def __init__(self, model, weight, size, resolution, scanning_speed, connection_interface):
        super().__init__(model, weight, size)
        self.type = self.__class__.__name__
        self.resolution = resolution
        self.scanning_speed = scanning_speed
        self.connection_interface = connection_interface

    @classmethod
    def set_item(cls):
        cls.model = input(f"Please enter model of Scanner:\n")
        cls.weight = cls.data_validation(input(f"Please enter weight or zero if unknown: \n"))
        cls.size = cls.data_validation(input(f"Please enter max size or zero if unknown: \n"))
        cls.resolution = input(f"Please enter max resolution for documents:\n")
        cls.scanning_speed = input(f"Please enter max available speed of scanning: \n")
        cls.connection_interface = input(f"Please enter connection interface: \n")
        print("Scanner data has been entered")
        return Scanner(cls.model, cls.weight, cls.size, cls.resolution, cls.scanning_speed, cls.connection_interface)

    def __str__(self):
        return f'Current office equipment type is {self.type}.\n' \
               f'Parameters are: \n' \
               f'model name is {self.model}\n' \
               f'weight is {self.weight}\n' \
               f'size is {self.size}\n' \
               f'Max resolution is {self.resolution}\n' \
               f'Max scanning speed is {self.scanning_speed}\n' \
               f'connection interface is {self.connection_interface}.'


class Copier(OfficeEquipment):
    def __init__(self, model, weight, size, print_type, scanning_speed, connection_interface):
        super().__init__(model, weight, size)
        self.type = self.__class__.__name__
        self.print_type = print_type
        self.scanning_speed = scanning_speed
        self.connection_interface = connection_interface

    @classmethod
    def set_item(cls):
        cls.model = input(f"Please enter model of Copier:\n")
        cls.weight = cls.data_validation(input(f"Please enter weight or zero if unknown: \n"))
        cls.size = cls.data_validation(input(f"Please enter max size or zero if unknown: \n"))
        cls.print_type = input(f"Please enter print type for documents:\n")
        cls.scanning_speed = input(f"Please enter max available speed of scanning: \n")
        cls.connection_interface = input(f"Please enter connection interface: \n")
        print("Copier data has been entered")
        return Copier(cls.model, cls.weight, cls.size, cls.print_type, cls.scanning_speed, cls.connection_interface)

    def __str__(self):
        return f'Current office equipment type is {self.type}.\n' \
               f'Parameters are: \n' \
               f'model name is {self.model}\n' \
               f'weight is {self.weight}\n' \
               f'size is {self.size}\n' \
               f'Print type is {self.print_type}\n' \
               f'Max scanning speed is {self.scanning_speed}\n' \
               f'connection interface is {self.connection_interface}.'
