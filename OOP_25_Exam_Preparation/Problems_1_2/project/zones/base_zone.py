from abc import ABC, abstractmethod

from typing import List

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: List[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        return sorted(self.ships, key=lambda x: (-x.hit_strength, x.name))

    @abstractmethod
    def zone_info(self):
        pass

    @property
    @abstractmethod
    def zone_type(self):
        pass

