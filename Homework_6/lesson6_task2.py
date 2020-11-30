"""Lesson 6 task 2"""


class Road:

    def __init__(self, width, length, layer=5, kind='normal'):
        self._width = width
        self._length = length
        self._layer = layer
        if kind == 'normal':
            self._density = 1100
        elif kind == 'mold':
            self._density = 1500
        elif kind == 'pressed':
            self._density = 2000
        elif kind == 'concrete':
            self._density = 2450
        else:
            self._density = 1100

    def weight_calc(self):
        # width mm -> * length km -> m * layer sm -> m density kg/m3
        return self._width / 1000 * self._length * 1000 * self._layer / 100 * self._density

    def print_data(self):
        print(f"Mass of road with entered parameters is {self.weight_calc()} kilogramms or {self.weight_calc()/1000} "
              f"metrical tonns")
