class vowels:
    VOW = "AaEeIiOoUuYy"

    def __init__(self, word):
        self.data = word
        self.next_index = -1

    @staticmethod
    def find_next_index(idx, word):
        for i in range(idx, len(word)):
            if word[i] in vowels.VOW:
                return i

    def __iter__(self):
        return self

    def __next__(self):
        self.next_index = self.find_next_index(self.next_index + 1, self.data)
        if self.next_index != None and self.next_index < len(self.data):
            cr = self.data[self.next_index]
            return cr
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
