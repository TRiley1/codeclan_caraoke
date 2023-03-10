class Room:

    def __init__(self,id):
        self.id  = id
        self.guests = []

    def add_guest(self,guest):
        self.guests.append(guest)

    def remove_guest(self,guest):
        self.guests.remove(guest)