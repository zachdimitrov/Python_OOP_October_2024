class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.id = id
        self.name = name
        self.is_rented = False

    @staticmethod
    def get_month(month):
        number = int(month)
        if number == 1:
            return "January"
        elif number == 2:
            return "February"
        elif number == 3:
            return "March"
        elif number == 4:
            return "April"
        elif number == 5:
            return "May"
        elif number == 6:
            return "June"
        elif number == 7:
            return "July"
        elif number == 8:
            return "August"
        elif number == 9:
            return "September"
        elif number == 10:
            return "October"
        elif number == 11:
            return "November"
        elif number == 12:
            return "December"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        try:
            month = cls.get_month(date.split(".")[1])
            year = int(date.split(".")[2])
        except IndexError:
            print("Date is wrong format - day.month.year!")

        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"
