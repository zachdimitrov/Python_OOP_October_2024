class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @staticmethod
    def convert_numbers(number):
        str_number = str(number)
        if number < 10:
            str_number = "0" + str_number
        return str_number

    @staticmethod
    def check_max(number, max_number):
        if number > max_number:
            number = 0
        return number

    def get_time(self):
        str_hours = self.convert_numbers(self.hours)
        str_mins = self.convert_numbers(self.minutes)
        str_secs = self.convert_numbers(self.seconds)
        return f"{str_hours}:{str_mins}:{str_secs}"

    def next_second(self):
        new_seconds = self.check_max(self.seconds + 1, self.max_seconds)
        if self.seconds == self.max_seconds:
            new_mins = self.check_max(self.minutes + 1, self.max_minutes)
        else:
            new_mins = self.minutes
        if self.minutes == self.max_minutes:
            new_hours = self.check_max(self.hours + 1, self.max_hours)
        else:
            new_hours = self.hours

        self.set_time(new_hours, new_mins, new_seconds)
        return self.get_time()


t = Time(1, 2, 3)
t.set_time(3, 2, 1)
time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
