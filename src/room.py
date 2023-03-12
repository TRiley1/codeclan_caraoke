class Room:

    def __init__(self,id,capacity):
        self.id  = id
        self.guests = []
        self.track_list = []
        self.capacity = capacity
        self.snacks = {} 
        self.tab = 0

    def remove_guest(self,guest):
        self.guests.remove(guest)

    def add_song(self,song):
        self.track_list.append(song)

    def check_fav(self):
        for guest in self.guests:
            if guest.fav_song in self.track_list:
                return "Yipee!"
            else:
                self.add_song(guest.fav_song) 

    def add_snack(self,snack,price):
        self.snacks[snack] = price

    def sell_snack(self,snack):
        self.tab += self.snacks[snack]
