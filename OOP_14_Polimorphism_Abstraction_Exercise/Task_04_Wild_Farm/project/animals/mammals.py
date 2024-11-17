from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "ROAR!!!"
