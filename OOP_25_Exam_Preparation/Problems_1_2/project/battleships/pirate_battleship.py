from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=80)

    def attack(self):
        self.ammunition -= 10
        if self.ammunition < 0:
            self.ammunition = 0

    @property
    def ship_type(self):
        return "PirateBattleship"

    @property
    def zone_type(self):
        return "PirateZone"
