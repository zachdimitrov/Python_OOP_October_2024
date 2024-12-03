from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, volume=8)

    def zone_info(self):
        result = f"@Pirate Zone Statistics@\n"
        result += f"Code: {self.code}; Volume: {self.volume}\n"
        result += f"Battleships currently in the Pirate Zone: {len(self.ships)}, " \
                  f"{len([x for x in self.ships if x.__class__.__name__ == 'RoyalBattleship'])} " \
                  f"out of them are Royal Battleships.\n"

        result += f"#{', '.join([x.name for x in self.get_ships()])}#"
        return result

    def __repr__(self):
        return "PirateZone"
