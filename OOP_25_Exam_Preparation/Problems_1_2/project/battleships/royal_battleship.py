from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=100)

    def attack(self):
        self.ammunition -= 25
        if self.ammunition < 0:
            self.ammunition = 0

    @property
    def ship_type(self):
        return "RoyalBattleship"

    @property
    def zone_type(self):
        return "RoyalZone"
