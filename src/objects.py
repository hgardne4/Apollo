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
# This is also a Table (See Above)
class Merch:
    # constuctor: 
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    # GETTERS:
    def get_item_name(self):
        return self.item_name
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity