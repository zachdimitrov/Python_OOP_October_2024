from abc import ABC
from project.animal import Animal

class Dog(Animal, ABC):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} "\
                f"year old {self.gender} {self.__class__.__name__}"
    