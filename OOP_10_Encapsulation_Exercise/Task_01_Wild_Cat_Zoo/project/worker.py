class Worker:
    def __init__(self, name: str, age: int, salary: int):
        self.salary = salary
        self.age = age
        self.name = name

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
