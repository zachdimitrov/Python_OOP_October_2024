from typing import List

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager():
    VALID_ZONES = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    SHIP_TYPES = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.VALID_ZONES:
            raise Exception("Invalid zone type!")

        for zone in self.zones:
            if zone.code == zone_code:
                raise Exception("Zone already exists!")

        new_zone = self.VALID_ZONES[zone_type](zone_code)
        self.zones.append(new_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.SHIP_TYPES:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        new_ship = self.SHIP_TYPES[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if ship.zone_type == zone.zone_type:
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        try:
            ship = [s for s in self.ships if s.name == ship_name][0]
        except IndexError:
            return "No ship with this name!"
        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attacking_ships = []
        defending_ships = []
        for ship in zone.ships:
            if ship.is_attacking:
                attacking_ships.append(ship)
            else:
                defending_ships.append(ship)

        try:
            attacker = sorted(attacking_ships, key=lambda x: -x.hit_strength)[0]
            defender = sorted(defending_ships, key=lambda x: -x.health)[0]
        except IndexError:
            return "Not enough participants. The battle is canceled."
        attacker.attack()
        defender.take_damage(attacker)
        if defender.health <= 0:
            zone.ships.remove(defender)
            self.ships.remove(defender)
            return f"{defender.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [x.name for x in self.ships if x.is_available]
        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{', '.join(available_ships)}#\n" if available_ships else ""
        result += "***Zones Statistics:***\n" \
            f"Total Zones: {len(self.zones)}\n"
        zones = sorted(self.zones, key=lambda x: x.code)
        result += "\n".join([z.zone_info() for z in zones])
        return result.strip()
