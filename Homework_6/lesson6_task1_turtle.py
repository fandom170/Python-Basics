import turtle
import time
import sys
import itertools


class TrafficLightTurtle:
    color_timings = {
        "RED": 7,
        "RED_YELLOW": 2,
        "BLACK": 0,
        "GREEN": 8,
        "OTHER": 0,
        "YELLOW": 2
    }

    __color = "red"

    def get_color(self):
        return self.__color

    def draw_circle(self, t, fillcolor):
        t.shapesize(1, 1, 1)
        t.pen(pencolor="black", fillcolor=fillcolor, pensize=10, speed=10)
        t.pendown()
        t.begin_fill()
        t.circle(60)
        t.end_fill()
        t.penup()

    def draw_light(self, t, chart):
        t.penup()
        self.draw_circle(t, chart[0])
        t.goto(0, -130)
        self.draw_circle(t, chart[1])
        t.goto(0, -260)
        self.draw_circle(t, chart[2])
        t.home()

    def draw_form(self, t):
        t.pen(pencolor="black", fillcolor="gray", pensize=3, speed=15)
        t.penup()
        t.goto(-70, 140)
        t.begin_fill()
        t.pendown()
        t.fd(140)
        t.rt(90)
        t.fd(410)
        t.rt(90)
        t.fd(140)
        t.rt(90)
        t.fd(410)
        t.end_fill()
        t.penup()
        t.home()

    def choose_light(self, current_color):
        if current_color == "RED":
            top = "red"
            middle, bottom = "black", "black"
        elif current_color == "RED_YELLOW":
            top = "red"
            middle = "yellow"
            bottom = "black"
        elif current_color == "YELLOW":
            top, bottom = "black", "black"
            middle = "yellow"
        elif current_color == "GREEN":
            top, middle = "black", "black"
            bottom = "green"
        else:
            top, middle, bottom = "black", "black", "black"

        return top, middle, bottom

    def running(self, interval):
        try:
            interval = float(interval)
        except ValueError:
            print("You entered wrong rime value")
            sys.exit(-1)
        # start of traffic light drawing
        s = turtle.getscreen()
        turtle.title("Traffic light")
        t = turtle.Turtle()
        start_time = time.time()
        self.draw_form(t)
        for k, v in itertools.cycle(self.color_timings.items()):
            color = self.choose_light(k)
            self.draw_light(t, color)
            time.sleep(v)
            if time.time() - start_time > interval:
                break


if __name__ == '__main__':
    light = TrafficLightTurtle()
    light.running(60)
