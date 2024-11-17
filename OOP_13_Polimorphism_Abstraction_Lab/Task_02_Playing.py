class Guitar:
    def play(self):
        return "Playing the guitar"


class Piano:
    def play(self):
        return "Playing the piano"


def start_playing(obj):
    return obj.play()


guitar = Guitar()
print(start_playing(guitar))