from abc import ABC, abstractmethod


class BaseClient(ABC):
    MEMBERSHIP_TYPES = ["Regular", "VIP"]

    def __init__(self, name: str, membership_type: str):
        self.membership_type = membership_type
        self.name = name
        self.points: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.MEMBERSHIP_TYPES:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        discount = 0
        if self.points >= 100:
            discount = 10
            self.points -= 100
        elif 50 <= self.points < 100:
            discount = 5
            self.points -= 50

        return discount, self.points


