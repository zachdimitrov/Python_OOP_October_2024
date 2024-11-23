class countdown_iterator:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if self.count >= -1:
            return self.count + 1
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
