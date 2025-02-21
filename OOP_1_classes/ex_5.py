class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.__a = 5

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics

    def __str__(self):
        return "New object way of printing"

song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
print(song.a)

