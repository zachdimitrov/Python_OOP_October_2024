from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    private_available_money = 25000.0
    private_available_space = 3000

    def __init__(self, name: str):
        super().__init__(name, self.private_available_money, self.private_available_space)

    def increase_money(self):
        self.available_money += 5000.0
