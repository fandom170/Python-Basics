"""Lesson 6 task 4 classes"""


class Car:
    __is_police = False

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def go(self, speed):
        self.speed = speed
        print(f"The car {self.name} started running with velocity {speed} km/h")

    def stop(self):
        self.speed = 0
        print(f"The car {self.name} stopped. Current speed is zero.")

    def turn(self, direction):
        print(f"The car {self.name} turned into {direction} direction.")

    def show_speed(self):
        print(f"current speed of car {self.name} is {self.speed} km/h.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Speed of car {self.name} is too large.")
        else:
            print(f"Current speed of car {self.name} is {self.speed} km/h.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Speed of car {self.name} is too large.")
        else:
            print(f"Current speed of car {self.name} is {self.speed} km/h.")


class PoliceCar(Car):
    __is_police = True
