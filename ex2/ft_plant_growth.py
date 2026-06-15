#!/usr/bin/env python3
import sys
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from ex1.ft_garden_data import Plant 


class Plant_week(Plant):
    def __init__(self, name, tole, day) -> None:
        super().__init__(name, tole, day)
        self.first = tole

    def grow(self) -> None:
        self.tole = round(self.tole + 0.8, 2)
        self.day += 1

    def total(self) -> None:
        print(
            f"{self.day}days old Growth this week: "
            f"{round(self.tole-self.first,2)}cm"
            )


rose = Plant_week("Rose", 25, 30)
print("=== Garden Plant Growth ===", end="")
rose.show()
for i in range(1, 8):
    print("== Day " + str(i) + " ===", end="")
    rose.grow()
    rose.show()
rose.total()
