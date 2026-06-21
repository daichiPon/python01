#!/usr/bin/env python3
class Plant:
    def __init__(self, name:str, height:int, day:int) -> None:
        self.name = name
        self.height = height
        self.day = day

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.day}days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Sunflowe = Plant("Sunflowe", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    Rose.show()
    Sunflowe.show()
    Cactus.show()
