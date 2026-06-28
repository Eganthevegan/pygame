class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []

    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")

rock_mix = Playlist("Road Trip Mix", "Pop")
del rock_mix