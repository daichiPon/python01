#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        self.name = name
        self.height = height
        self.day = day
        self.first = height

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day}days old")

    def grow(self, daygrow: int) -> None:
        self.daygrow = daygrow
        self.height = round(self.height + self.daygrow, 2)
        self.day += 1

    def total(self) -> None:
        print(
            f"{self.day}days old Growth this week: "
            f"{round(self.height-self.first,2)}cm"
        )


if __name__ == "__main__":
    p_arr = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("== Plant Factory Output ===")
    for plant in p_arr:
        print("Created:", end="")
        plant.show()
