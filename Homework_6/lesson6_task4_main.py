"""Lesson 6 task 4 main"""
# import lesson6_task4
from Homework_6 import lesson6_task4 as cars

tc = cars.TownCar('Lincoln Towncar', 25, 'black')
pc = cars.PoliceCar('Chrysler 300', 65, 'white-blue')
wc = cars.WorkCar("ГАЗ Газель", 0, "dirty-grey")
sc = cars.SportCar("Ford Mustang", 0, "blue-black")

print(tc.color)
print(pc.name)

wc.show_speed()
wc.speed = 39
wc.show_speed()
sc.turn("left")
