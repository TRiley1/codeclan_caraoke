class Guest: 
    def __init__(self, name, fav_song, wallet):
        self.name = name 
        self.fav_song = fav_song
        self.wallet = wallet

    def pay(self, money):
        if self.wallet >= money:
            self.wallet -= money 

