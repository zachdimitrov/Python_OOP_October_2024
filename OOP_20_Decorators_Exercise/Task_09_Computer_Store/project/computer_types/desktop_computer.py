from project.computer_types.computer import Computer


class DesktopComputer(Computer):
<<<<<<< HEAD
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
=======
    @property
    def processors(self):
        return {"AMD Ryzen 7 5700G": 500,
                "Intel Core i5-12600K": 600,
                "Apple M1 Max": 1800}

    @property
    def max_ram(self):
        return 128

    @property
    def computer_type(self):
        return "desktop computer"
>>>>>>> 0c1845752dbbc813e7100b8d132b86d01471b4f4
