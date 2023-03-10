class Room:

    def __init__(self,id,capacity):
        self.id  = id
        self.guests = []
        self.track_list = []
        self.capacity = capacity

    def add_guest(self,guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        return "Capacity Full"

    def remove_guest(self,guest):
        self.guests.remove(guest)

    def add_song(self,song):
        self.track_list.append(song)