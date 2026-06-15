class Plant:
    def __init__(self, name, tole, day) -> None:
        self.name = name
        self.tole = tole
        self.day = day

    def show(self) -> None:
        print(f"{self.name}: {self.tole}cm, {self.day}days old", end="")


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Sunflowe = Plant("Sunflowe", 80, 45)
    Cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===", end=(" "))
    Rose.show()
    Sunflowe.show()
    Cactus.show()
