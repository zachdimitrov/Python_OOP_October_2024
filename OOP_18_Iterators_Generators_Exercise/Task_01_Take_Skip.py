class take_skip:
    def __init__(self, step: int, count: int):
        self.count = count
        self.step = step
        self.current_count = 0
        self.next_number = 0 - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.current_count += 1
        self.next_number += self.step
        if self.current_count <= self.count:
            return self.next_number
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
numbers = take_skip(10, 5)
for number in numbers:
    print(number)


