"""
OBJECT ORIENTATION:
"""
# BAND OBJECT -> a band has a name, genre, set of merchendise (for right now)
class Band:
    # constructor: needs an name, genre
    def __init__(self, name, genre, merch_items):
        self.name = name
        self.genre = genre
        self.merch_items = merch_items
        self.albums = []

    # function to add an album to the band
    def add_album(self, album):
        self.albums.append(album)

    def add_merch_item(self, item):
        self.merch_items.append(item)

    # GETTERS:
    def get_name(self):
        return self.name
    def get_genre(self):
        return self.genre
    def get_merch(self):
        return self.merch_items
    def get_albums(self):
        return self.albums

# ALBUM OBJECT -> album has a name, genre, and a list of songs (for right now)
class Album:
    # constuctor: 
    def __init__(self, name, genre, songs):
        self.name = name
        self.genre = genre
        self.songs = songs

    # GETTERS:
    def get_name(self):
        return self.name
    def get_genre(self):
        return self.genre
    def get_songs(self):
        return self.songs

# MERCH OBJECT -> a merchendise item has a name and price (for right now)
class Merch:
    # constuctor: 
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

    # GETTERS:
    def get_item_name(self):
        return self.item_name
    def get_price(self):
        return self.price

merch = []
for i in range(10):
    temp = Merch('t-shirt', i*30)
    merch.append(temp)

band = Band("Beach House", "dream pop", merch)
album = Album("Depression Cherry", "dream pop", ['PPP', 'Space Song', 'Beyond Love'])
band.add_album(album)
album = Album("Bloom", "dream pop", ['Other People', 'Lazuli', 'Irene'])
band.add_album(album)
for album in band.get_albums():
    print(album.get_name())
for item in band.get_merch():
    print(item.get_item_name())
    print(item.get_price())
