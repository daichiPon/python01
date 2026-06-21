#!/usr/bin/env python3
class Plant:
    show_count = 0
    grow_count = 0
    age_count = 0

    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0

    def grow(self, daygrow) -> None:
        self.daygrow = daygrow
        self.grow_count += 1
        self._height = round(self._height + self.daygrow, 2)

    def age(self, dayage) -> None:
        self.dayage = dayage
        self.age_count += 1
        self._age += self.dayage

    def get_heigh(self) -> float:
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
        self.show_count += 1
        print(f"{self.name}: {self._height}cm, {self._age}days old")
    
    @classmethod
    def class_show(cls) -> None:
        cls.show_count += 1
        print("Unknown plant: 0.0cm, 0 days old")

    @classmethod
    def class_statistical_data(cls) -> None:
        print(f"Stats: {cls.grow_count} grow, {cls.age_count} age, {cls.show_count} show")

    def total(self) -> None:
        print(
            f"{self.day}days old Growth this week: "
            f"{round(self.tole-self.first,2)}cm"
        )

    @staticmethod
    def check_year(age):
        if age >= 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")


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

    def statistical_data(self):
        print(f"Stats: {self.grow_count} grow, {self.age_count} age,", end="")
        print(f"{self.show_count} show")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        self.shade_count += 1
        print(f"Tree Oak now produces a shade of {self._height}cm", end="")
        print(f"long and {self.trunk_diameter}cm wide")

    def statistical_data(self):
        print(f"Stats: {self.grow_count} grow, {self.age_count} age,", end="")
        print(f"{self.show_count} show")
        print(f"{self.shade_count} shade")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        self.seeds += 42
        super().bloom()

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

    def statistical_data(self):
        print(f"Stats: {self.grow_count} grow, {self.age_count} age,", end="")
        print(f"{self.show_count} show")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year(30)
    Plant.check_year(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose.statistical_data()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose.statistical_data()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5)
    oak.show()
    print("[statistics for Oak]")
    oak.statistical_data()
    print("[asking the oak to produce shade")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.statistical_data()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.bloom()
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower.statistical_data()

    print("\n=== Anonymous")
    Plant.class_show()
    print("[statistics for Unknown plant]")
    Plant.class_statistical_data()
    