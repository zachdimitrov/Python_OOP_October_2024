from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp():
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    @property
    def valid_types(self):
        return ["Desktop Computer", "Laptop"]

    def build_computer(self, type_computer: str,
                       manufacturer: str,
                       model: str,
                       processor: str,
                       ram: int):
        if type_computer not in self.valid_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == self.valid_types[0]:
            computer = DesktopComputer(manufacturer, model)
        else:
            computer = Laptop(manufacturer, model)

        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        self.profits += computer.price
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for pc in self.warehouse:
            if pc.price <= client_budget and \
                    pc.processor == wanted_processor and \
                    pc.ram >= wanted_ram:
                difference = client_budget - pc.price
                self.profits += difference
                self.warehouse.remove(pc)
                return f"{pc} sold for {client_budget}$."
        raise Exception("Sorry, we don't have a computer for you.")
