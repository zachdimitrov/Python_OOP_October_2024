from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.food_eaten = 0
        self.weight = weight
        self.name = name


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return (f"{self.__class__.__name__} [{self.name}, {self.wing_size}, "
                f"{self.weight}, {self.food_eaten}]")


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return (f"{self.__class__.__name__} [{self.name}, {self.weight}, "
                f"{self.living_region}, {self.food_eaten}]")
