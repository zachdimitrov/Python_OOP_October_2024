class sequence_repeat:
    def __init__(self, sequence, number):
        self.number = number
        self.sequence = sequence
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= self.number:
            idx = self.i
            if idx > len(self.sequence):
                idx = idx % len(self.sequence)
            return self.sequence[idx - 1]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
