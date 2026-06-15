class Plant:
    def __init__(self, name, height, age):
        self.name = name,
        self._height = height,
        self._age = age,

    def get_heigh(self) -> float:
        return self._height
    
    def get_age(self) -> int:
        return self._age
    
    def set_heigh(self,tole) -> None:
        if tole < 0:
            self._tole = tole
        else:
            self._tole = tole
            print("height can't be negative Height update rejected Rose: Error")
    
    def set_age(self,age) -> None:
        if age < 0:
            print(f"")
        else:
            self._age = age
            print(f"age can't be negative Age update rejected Current state:${self.name}: ${self._height}cm, ${self._age} days old")

