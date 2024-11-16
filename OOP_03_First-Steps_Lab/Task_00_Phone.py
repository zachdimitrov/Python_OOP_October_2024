class Phone:
    def __init__(self, color, size, pixels=1060):
        self.color = color
        self.size = size
        self.camera = pixels

    def turn_on(self):
        return "The phone is turned on"


phone1 = Phone("black", 10, 2000)
phone2 = Phone("yellow", 5)
print(phone1.color)
print(phone1.turn_on())

