class Plant:
    def __init__(self, name, tole, day) -> None:
        self.name = name
        self.tole = tole
        self.day = day

    def show(self) -> None:
        print(f"{self.name}: {self.tole}cm, {self.day}days old", end="")

    def grow(self) -> None:
        self.tole = round(self.tole + 0.8, 2)
        self.day += 1

    def total(self) -> None:
        print(
            f"{self.day}days old Growth this week: "
            f"{round(self.tole-self.first,2)}cm"
            )


if __name__ == "__main__":
    p_arr = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    for plant in p_arr:
        plant.show()
