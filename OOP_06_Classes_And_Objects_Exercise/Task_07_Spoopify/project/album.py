from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = []
        if songs:
            for song in songs:
                self.songs.append(song)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        else:
            if not song.single:
                self.songs.append(song)
                return f"Song {song.name} has been added to the album {self.name}."
            else:
                return f"Cannot add {song.name}. It's a single"

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return "Song is not in the album."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result
