from project.animals.animal import Mammal
from project.food import Food, Meat, Seed, Vegetable, Fruit


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if not (isinstance(food, Vegetable) or isinstance(food, Fruit)):
            return f"Mouse does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"Dog does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if not (isinstance(food, Vegetable) or isinstance(food, Meat)):
            return f"Cat does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.living_region = living_region
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"Tiger does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 1.00
        self.food_eaten += food.quantity