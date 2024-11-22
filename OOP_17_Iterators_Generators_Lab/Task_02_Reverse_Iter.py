class reverse_iter:
    def __init__(self, obj):
        self.data = obj
        self.start_index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index -= 1
        if self.start_index >= 0:
            return self.data[self.start_index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

