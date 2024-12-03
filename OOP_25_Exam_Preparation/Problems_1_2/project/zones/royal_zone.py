from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=10)

    def zone_info(self):
        result = f"@Royal Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += f"Battleships currently in the Royal Zone: {len(self.ships)}, " \
                  f"{len([x for x in self.ships if x.ship_type == 'PirateBattleship'])} " \
                  f"out of them are Pirate Battleships."
        ordered = self.get_ships()
        result += f"\n#{', '.join([x.name for x in ordered])}#" if ordered else ""
        return result

    @property
    def zone_type(self):
        return "RoyalZone"
