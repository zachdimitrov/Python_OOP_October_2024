from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                if r.capacity >= people and not r.is_taken:
                    r.take_room(people)
                    self.guests += people

    def free_room(self, room_number):
        for r in self.rooms:
            if r.number == room_number:
                guests = r.guests
                r.free_room()
                self.guests -= guests

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
            f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}\n" \
            f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}"

