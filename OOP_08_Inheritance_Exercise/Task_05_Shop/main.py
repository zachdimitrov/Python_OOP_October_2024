from project.drink import Drink
from project.food import Food
from project.product import Product
from project.product_repository import ProductRepository

food1 = Food("apple")
drink1 = Drink("water")
repo = ProductRepository()
repo.add(food1)
repo.add(drink1)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)

product = Product('product', 150)
drink = Drink('drink')
food = Food('food')
repo = ProductRepository()
print(product.name)  # 'product'
print(product.quantity)  # 150
product.decrease(10)
print(product.quantity)  # 140
product.increase(10)
print(product.quantity)  # 160
print(drink.name)  # 'drink'
print(drink.quantity)  # 10
print(drink.__class__.__base__.__name__)  # 'Product'