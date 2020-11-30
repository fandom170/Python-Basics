"""Lesson 6 task 1 classes"""
from enum import Enum
import time
from itertools import cycle
import sys


class Colorings(Enum):
    RED = "\033[91m"
    RED_YELLOW = "\033[33m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    BLINK = "\033[5m"
    RESET = "\033[0m"


class TrafficLight:
    color_timings = {
        "RED": 7,
        "RED_YELLOW": 2,
        "GREEN": 8,
        "YELLOW": 2
    }

    _color = "RED"

    def running(self, interval):
        try:
            interval = float(interval)
        except ValueError:
            print("You entered wrong rime value")
            sys.exit(-1)
        start_time = time.time()
        for k, v in cycle(self.color_timings.items()):
            self._color = k
            print("{}Current traffic light color is {}".format(Colorings[k].value, self._color))
            print(f"Color will be changed in {v} seconds")
            time.sleep(v)
            if time.time() - start_time > interval:
                break

    def get_color(self):
        return self._color

    def set_color(self, color):
        if color in self.color_timings.keys():
            self._color = color
        else:
            print("No such color!")
