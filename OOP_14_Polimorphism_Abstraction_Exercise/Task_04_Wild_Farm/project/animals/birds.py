from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        self.wing_size = wing_size
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        self.wing_size = wing_size
        self.weight = weight
        self.name = name

    @staticmethod
    def make_sound():
        return "Cluck"
