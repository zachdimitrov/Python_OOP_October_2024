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

    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
