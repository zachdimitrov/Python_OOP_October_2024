from project.product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self.milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

    @milliliters.setter
    def milliliters(self, value):
        if value > 0:
            self.__milliliters = value
        else:
            raise ValueError("Milliliters cannot be zero or negative!")

