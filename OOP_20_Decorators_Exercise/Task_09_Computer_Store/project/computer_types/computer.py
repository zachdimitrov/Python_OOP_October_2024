import math
from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.price: int = 0
        self.ram: int or None = None
        self.processor: str or None = None
        self.model = model
        self.manufacturer = manufacturer

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def processors(self):
        pass

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def computer_type(self):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    def is_valid_ram(self, n):
        if n & (n - 1) == 0 and (2 <= n <= self.max_ram):
            return True
        return False

    def configure_computer(self, processor: str, ram: int):
        if not self.is_valid_ram(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")
        if processor not in self.processors.keys():
            raise ValueError(f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")
        self.processor = processor
        processor_price = self.processors[processor]
        self.price += int(processor_price)
        self.ram = ram
        ram_price = int(math.log2(ram) * 100)
        self.price += ram_price
        return f"Created {self.__repr__()} for {self.price}$."
