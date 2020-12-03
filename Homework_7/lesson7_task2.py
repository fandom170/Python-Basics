"""Lesson 7 task 2 """
from abc import abstractmethod, ABC


class Wearing(ABC):

    @abstractmethod
    def required_amt_calc(self):
        pass

    @abstractmethod
    def get_called_name(self):
        pass


class Clothes(Wearing):
    def __init__(self, size):
        self.size = size
        self.name = self.get_called_name()

    @property
    def get_size(self):
        return "{} of current {} is {}".format("Size" if self.name == "Coat" else "Height",
                                               self.name.lower(), self.size)

    def get_called_name(self):
        return self.__class__.__name__

    def required_amt_calc(self):
        if self.name == "Coat":
            return (self.size / 6.5) + 0.5
        elif self.name == "Suite":
            return (2 * self.size) + 0.3

    def __str__(self):
        return f'Amount of material which is needed for {self.name} creation is ' \
               f'{round(self.required_amt_calc(), 2)} square meters.'


class Coat(Clothes):
    pass


class Suite(Clothes):
    pass


coat = Coat(1)
print(coat.get_size)
print(coat)

suite = Suite(2.5)
print(suite.get_size)
print(suite)
