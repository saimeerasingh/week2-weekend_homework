class Room:
    def __init__(self,name,till,ticket_price,capcity,songs):
        self.name = name
        self.till = till
        self.ticket_price = ticket_price
        self.capcity = capcity
        self.songs = songs
        self.guest_lists = []
       
    
    def add_song_to_list(self,song):
        self.songs.append(song)

    def remove_song_from_list(self,song):
        self.songs.remove(song)

    def add_money_to_till(self,amount):
        amount = self.ticket_price
        self.till += amount

    