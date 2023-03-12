class Room:

    def __init__(self,id,capacity):
        self.id  = id
        self.guests = []
        self.track_list = []
        self.capacity = capacity

    def remove_guest(self,guest):
        self.guests.remove(guest)

    def add_song(self,song):
        self.track_list.append(song)