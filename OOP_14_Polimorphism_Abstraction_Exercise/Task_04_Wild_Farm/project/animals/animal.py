from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, food_eaten=0):
        self.food_eaten = food_eaten
        self.weight = weight
        self.name = name


class Bird(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

