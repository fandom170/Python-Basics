"""Lesson 6 task 5 classes"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Drawing is running.")


class Pen(Stationery):

    def draw(self):
        print(f"Drawing by pencil. Pencil {self.title} os very good pencil.")


class Pencil(Stationery):
    def draw(self):
        print(f"Drawing by Pen. Pen {self.title} os very good pen.")


class Handle(Stationery):
    def draw(self):
        print(f"Drawing by handle. Handle {self.title} os very good handle.")


stationery = Stationery("Something")
pen = Pen("Space Pen")
pencil = Pencil("KOOH-I-NOOR")
handle = Handle("Edding")

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
