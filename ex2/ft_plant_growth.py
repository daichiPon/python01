#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day
        self.first = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day}days old")

    def grow(self, daygrow:int) -> None:
        self.daygrow = daygrow
        self.height = round(self.height + self.daygrow, 2)
        self.day += 1

    def total(self) -> None:
        print(f"Growth this week: {round(self.height-self.first,2)}cm")


rose = Plant("Rose", 25, 30)
print("=== Garden Plant Growth ===")
rose.show()
for i in range(1, 8):
    print("== Day " + str(i) + " ===")
    rose.grow(0.8)
    rose.show()
rose.total()
