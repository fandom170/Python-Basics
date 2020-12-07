"""Lesson 8 task 1"""
from datetime import datetime


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"

    @classmethod
    def set_date(cls, string_date):
        try:
            init_date = Date.date_validation(string_date)
            return cls(init_date.day, init_date.month, init_date.year)
        except AttributeError:
            print("Entered date was incorrect or not a date at all.")

    @staticmethod
    def date_validation(data):
        try:
            return datetime.strptime(data, '%d-%m-%Y')
        except ValueError:
            return None


newDate = Date.set_date('01-05-2020')
print(newDate)
newDate1 = Date.set_date('45-05-2020')
newDate2 = Date.set_date('the milk')
