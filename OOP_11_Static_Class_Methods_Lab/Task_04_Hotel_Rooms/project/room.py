class Room:
    def __init__(self, number: int, capacity: int):
        self.capacity = capacity
        self.number = number
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int):
        if self.is_taken or self.capacity < people:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests = people

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
        else:
            return f"Room number {self.number} is not taken"
