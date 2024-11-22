from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Pig(Animal):
    def make_sound(self):
        return "gruh"


class Chicken(Animal):
    def make_sound(self):
        return "piu"


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Pig(), Chicken()]
animal_sound(animals)
