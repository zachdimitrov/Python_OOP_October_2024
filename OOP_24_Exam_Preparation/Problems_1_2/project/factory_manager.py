from project.products.base_product import BaseProduct
from project.stores.base_store import BaseStore
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:

    VALID_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.income = 0.0
        self.name = name
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_TYPES.keys():
            raise Exception("Invalid product type!")
        product = self.VALID_TYPES[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.STORE_TYPES.keys():
            raise Exception(f"{store_type} is an invalid type of store!")
        store = self.STORE_TYPES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        sell_type = ""
        if store.store_type == "FurnitureStore":
            sell_type = "Furniture"
        elif store.store_type == "ToyStore":
            sell_type = "Toys"
        purchased = 0
        for product in products:
            if product.sub_type == sell_type:
                store.products.append(product)
                self.products.remove(product)
                store.capacity -= 1
                purchased += 1
                self.income += product.price

        if purchased > 0:
            return f"Store {store.name} successfully purchased {purchased} items."
        return f"Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        try:
            store = [x for x in self.stores if x.name == store_name][0]
        except IndexError:
            raise Exception("No such store!")

        if len(store.products) > 0:
            return "The store is still having products in stock! Unregistering is inadvisable."
        name = store.name
        location = store.location
        self.stores.remove(store)
        return f"Successfully unregistered store {name}, location: {location}."

    def discount_products(self, product_model: str):
        discounted = 0
        for product in self.products:
            if product.model == product_model:
                product.discount()
                discounted += 1
        return f"Discount applied to {discounted} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        try:
            store = [x for x in self.stores if x.name == store_name][0]
        except IndexError:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        result = f"Factory: {self.name}\n"
        result += f"Income: {self.income:.2f}\n"
        result += f"***Products Statistics***\n"
        result += f"Unsold Products: {len(self.products)}. Total net price: {sum([x.price for x in self.products]):.2f}\n"
        models_pieces = {}
        for f in self.products:
            if f.model not in models_pieces.keys():
                models_pieces[f.model] = 1
            else:
                models_pieces[f.model] += 1
        models_pieces = dict(sorted(models_pieces.items(), key=lambda x: x[0]))
        for mod, pc in models_pieces.items():
            result += f"{mod}: {pc}\n"
        result += f"***Partner Stores: {len(self.stores)}***\n"
        sorted_stores = sorted(self.stores, key=lambda x: x.name)
        for store in sorted_stores:
            result += f"{store.name}\n"

        return result.strip()
