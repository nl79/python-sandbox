class Song:
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song Init method
        Args:
            title (str): Initializes the 'title' attribute
            artist (Artist): An artist object representing the song's creator.
            duration (Optional[int]): Initial value for the 'duration' attribute
                Will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("./fixtures/albums.txt") as albums:
        for line in albums:
            # data row should const of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if(new_artist is None):
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # we've just read details for a new artist
                # store the current album in the current artists collection then create a new arist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # we've just read a new album for the current artist
                # store the current album in the artist collection and create a new album object.
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to the current albumb collection.
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # after reading the last line of the textfile, we will have an artist and album that haven't been stored
        # process them now.
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list



def create_chechfile(artist_list):
    with open("./fixtures/checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                                                                           file=checkfile)

if __name__ == "__main__":
    artists = load_data()

    print("there are {} artists".format(len(artists)))

    create_chechfile(artists)
#help(Song.__init__);
# print(Song.__doc__)
# print(Song.__init__.__doc__)