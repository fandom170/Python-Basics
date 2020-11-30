"""Lesson 6 task 3 classes"""


class Worker:
    first_name = "Jacob"
    last_name = "Gardner"
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname):
        self.first_name = name
        self.last_name = surname


class Position(Worker):
    def __init__(self, first_name, last_name, income, bonus):
        super().__init__(first_name, last_name)
        self._income["wage"] = income
        self._income["bonus"] = bonus

    def get_full_name(self):
        return f"Full name of employee is {self.first_name} {self.last_name}"

    def get_total_income(self):
        salary = self._income['wage']
        bonus = self._income['bonus']
        print(f"Total worker {self.first_name} {self.last_name} income is "
              f"{salary + bonus}")


class PositionInherited(Worker):
    def __init__(self, income, bonus):
        super().__init__(Worker.first_name, Worker.last_name)
        self._income["wage"] = income
        self._income["bonus"] = bonus

    def get_full_name(self):
        return f"Full name of employee is {self.first_name} {self.last_name}"

    def get_total_income(self):
        salary = self._income['wage']
        bonus = self._income['bonus']
        print(f"Total worker {self.first_name} {self.last_name} income is "
              f"{salary + bonus}")


wc = Worker("John", "Smith")
ps = Position("Mark", "Smith", 100, 150)
psh = PositionInherited(300, 280)
ps.get_total_income()
print(ps.get_full_name())
psh.get_total_income()
print(psh.get_full_name())
