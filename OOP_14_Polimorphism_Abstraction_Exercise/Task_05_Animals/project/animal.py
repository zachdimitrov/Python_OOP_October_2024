from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int, gender: str):
        self.gender = gender
        self.age = age
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
