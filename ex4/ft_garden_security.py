#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def get_heigh(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_heigh(self, height) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age update: {self._age}days")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age}days old", end="")

    def grow(self) -> None:
        self.tole = round(self.tole + 0.8, 2)
        self.day += 1

    def total(self) -> None:
        print(
            f"{self.day}days old Growth this week: "
            f"{round(self.tole-self.first,2)}cm"
        )


if __name__ == "__main__":
    p = Plant("Rose", 15, 10)
    print(" === Garden Security System ====")
    print("Plant created: ", end="")
    p.show()
    print("\n")
    p.set_heigh(25)
    p.set_age(30)
    p.set_heigh(-1)
    p.set_age(-1)
    print("\nCurrent state:", end="")
    p.show()
