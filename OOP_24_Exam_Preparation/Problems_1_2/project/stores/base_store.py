import string
from abc import ABC, abstractmethod
from project.products.base_product import BaseProduct


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.capacity = capacity
        self.location = location
        self.name = name
        self.products: list[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value) != 3 or not value.isalnum():
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value
        
    def get_estimated_profit(self):
        all_price = sum([x.price for x in self.products])
        profit = all_price * 0.1
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        pass

    def store_stats(self):
        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
        result += f"{self.get_estimated_profit()}\n"
        if self.store_type == "FurnitureStore":
            type_for_sale = "Furniture"
        else:
            type_for_sale = "Toys"
        result += f"**{type_for_sale} for sale:\n"
        models_pieces = {}

        for f in self.products:
            if f.model not in models_pieces.keys():
                models_pieces[f.model] = {"pc": 1, "total": 0.0}
            else:
                models_pieces[f.model]["pc"] += 1
                models_pieces[f.model]["total"] += f.price
        models_pieces = dict(sorted(models_pieces.items(), key=lambda x: x[0]))
        for mod, detail in models_pieces.items():
            result += f"{mod}: {detail['pc']}pcs, average price: {detail['total'] / detail['pc']:.2f}\n"

        return result.strip()



