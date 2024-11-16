class PhotoAlbum:
    SLOTS = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @staticmethod
    def find_slot(m, pages, slots):
        for i in range(pages):
            if len(m[i]) < slots:
                return i, len(m[i]) - 1
        return None

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // PhotoAlbum.SLOTS + photos_count % PhotoAlbum.SLOTS
        return cls(pages)

    def add_photo(self, label: str):
        next_slot = self.find_slot(self.photos, self.pages, self.SLOTS)
        if next_slot:
            self.photos[next_slot[0]].append(label)
            return f"{label} photo added successfully on page {next_slot[0] + 1} slot {next_slot[1] + 1}"
        else:
            return "No more free slots"

    def display(self):
        result = "-"*11 + "\n"
        for i in range(self.pages):
            if self.photos[i]:
                for j in range(len(self.photos[i])):
                    result += "[] "
            if result[-1] == " ":
                result = result[:-1]
            result += "\n"
            result += "-"*11 + "\n"
        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
