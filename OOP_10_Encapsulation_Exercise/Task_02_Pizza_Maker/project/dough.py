class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.weight = weight
        self.baking_technique = baking_technique
        self.flour_type = flour_type

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("The weight cannot be less or equal to zero")

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value):
        if value:
            self.__flour_type = value
        else:
            raise ValueError("The flour type cannot be an empty string")

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if value:
            self.__baking_technique = value
        else:
            raise ValueError("The baking technique cannot be an empty string")
