from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    museum_available_money = 15000.0
    museum_available_space = 2000

    def __init__(self, name: str):
        super().__init__(name, self.museum_available_money, self.museum_available_space)

    def increase_money(self):
        self.available_money += 1000.0

