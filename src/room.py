class Room:

    def __init__(self,id):
        self.id  = id
        self.guests = []
        self.track_list = []

    def add_guest(self,guest):
        self.guests.append(guest)

    def remove_guest(self,guest):
        self.guests.remove(guest)

    def add_song(self,song):
        self.track_list.append(song)