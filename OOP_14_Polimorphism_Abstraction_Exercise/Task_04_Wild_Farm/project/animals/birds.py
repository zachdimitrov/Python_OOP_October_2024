from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.wing_size = wing_size
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"Owl does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.wing_size = wing_size
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity
