from abc import abstractmethod, ABC


class Clothes(ABC):
    pass


class Wearing(Clothes):

    def __init__(self, size):
        self._size = size
        self._consumption = (2 * self._size) + 0.3
        self._title = self.__class__.__name__

    @property
    def consumption(self):
        print("required amount is:")
        if self._title == "Coat":
            self._consumption = round((self._size / 6.5) + 0.5, 2)
        return self._consumption


class Coat(Wearing):
    pass


class Suite(Wearing):
    pass


coat = Coat(2)
print(coat.consumption)

suite = Suite(2)
print(suite.consumption)
