# Polymorphism example

class Shape:
    def calculate_area(self):
        return None


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


# Overload len example - magi method __len__

class MyClass:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __len__(self):
        return self.size


my_class = MyClass("Class Name", 3)
print(len(my_class))


# Overload add example - magic method __add__

class Purchase:
    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other):
        name = f'{self.product_name}, {other.product_name}'
        cost = self.cost + other.cost
        return Purchase(name, cost)

    def __repr__(self):
        return f"name: {self.product_name}, cost: {self.cost}"


first_purchase = Purchase('sofa', 650)
second_purchase = Purchase('table', 150)
print(first_purchase + second_purchase)

# Overload comparis0n __gt__ >

class Person:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name

    def __gt__(self, other):
        return self.salary > other.salary


person_one = Person('John', 20)
person_two = Person('Natasha', 35)
print(person_one > person_two)
