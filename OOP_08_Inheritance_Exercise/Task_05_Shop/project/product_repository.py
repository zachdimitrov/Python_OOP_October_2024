from typing import List, Optional
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        return next((p for p in self.products if p.name == product_name), None)
        # for p in self.products:
        #     if p.name == product_name:
        #         return p

    def remove(self, product_name: str):
        p = self.find(product_name)
        if p:
            self.products.remove(p)

    def __repr__(self):
        return "\n".join([f"{p}: {p.quantity}" for p in self.products])
        # result = ""
        # for p in self.products:
        #     result += f"{p}: {p.quantity}\n"
        # return result

