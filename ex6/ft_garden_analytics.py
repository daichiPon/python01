class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._count_grow = 0
            self._count_age = 0
            self._count_show = 0

        def record_grow(self) -> None:
            self._count_grow += 1

        def record_age(self) -> None:
            self._count_age += 1

        def record_show(self) -> None:
            self._count_show += 1

        def display(self) -> None:
            print(f"Stats: {self._count_grow} grow, "
                  f"{self._count_age} age, {self._count_show} show")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = self._Stats()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {round(self._height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {round(self._age)} days")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats.record_show()

    def grow(self, amount: float) -> None:
        self._height = round(self._height + amount, 1)
        self._stats.record_grow()

    def age(self, days: int) -> None:
        self._age += days
        self._stats.record_age()

    @staticmethod
    def ft_year(age: int) -> bool:
        return age >= 365

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show_stats(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self, _: int = 0) -> None:
        self.is_bloomed = True


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._count_shade = 0

        def record_shade(self) -> None:
            self._count_shade += 1

        def display(self) -> None:
            super().display()
            print(f" {self._count_shade} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._stats: Tree._Stats = Tree._Stats()
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height()}cm long and {self.trunk_diameter}cm wide."
        )
        self._stats.record_shade()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.num_seeds = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.num_seeds}")

    def bloom(self, num_seeds: int = 0) -> None:
        self.is_bloomed = True
        self.num_seeds = num_seeds


def display_stats(plant: Plant) -> None:
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    age = 30
    print(f"Is {age} days more than a year? -> {Plant.ft_year(age)}")
    age = 400
    print(f"Is {age} days more than a year? -> {Plant.ft_year(age)}")
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"[statistics for {rose.name}]")
    rose.show_stats()
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose.name}]")
    rose.show_stats()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak.name}]")
    oak.show_stats()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak.name}]")
    oak.show_stats()

    print("\n=== Seed")
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow(30)
    seed.age(20)
    seed.bloom(42)
    seed.show()
    print("[statistics for Sunflower]")
    seed.show_stats()

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous_plant()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)
