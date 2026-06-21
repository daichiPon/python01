#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def grow(self, daygrow) -> None:
        self.daygrow = daygrow
        self._height = round(self._height + self.daygrow, 2)

    def age(self) -> None:
        self._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_heigh(self, height) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be")
            print("negative Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be")
            print("negative Age update rejected")
        else:
            self._age = age
            print(f"Age update: {self._age}days")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age}days old")

    def total(self) -> None:
        print(
            f"{self.day}days old Growth this week: "
            f"{round(self.tole-self.first,2)}cm"
        )


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        self.color = color
        self.bloo = False
        super().__init__(name, height, age)

    def bloom(self) -> None:
        self.bloo = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloo:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        self.trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height}cm", end="")
        print(f"long and {self.trunk_diameter}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def grow(self, grow_num) -> None:
        self.grow_num = grow_num
        super().grow(self.grow_num)
        self.nutritional_value += 0.5


if __name__ == "__main__":
    f = Flower("Rose", 15.0, 10, "red")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    f.show()
    print("[asking the rose to bloom]")
    f.bloom()
    f.show()
    t = Tree("Oak", 200.0, 365, 5.0)
    print("\n=== Tree")
    t.show()
    print("[asking the oak to produce shade]")
    t.produce_shade()
    v = Vagetabel("Tomato", 5.0, 10, "April")
    print("\n=== Vegetable")
    v.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        v.age()
        v.grow(0.8)
    v.show()
