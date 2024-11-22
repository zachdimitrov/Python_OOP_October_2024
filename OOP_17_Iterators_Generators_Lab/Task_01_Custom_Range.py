class CustomRange:
    def __init__(self, start, end):
        self.end = end
        self.start = start
        self.current = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.end:
            return self.current
        self.current = self.start - 1 # allows multiple iterations
        raise StopIteration


one_to_ten = CustomRange(1, 10)
for num in one_to_ten:
    print(num)

for num in one_to_ten:
    print(num)
