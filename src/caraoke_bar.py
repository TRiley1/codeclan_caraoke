class CaraokeBar:
    def __init__(self, name, till, entry_fee):
        self.name = name
        self.till = till 
        self.entry_fee = entry_fee
        self.booths = []

    def add_room_to_booth(self, room):
        self.booths.append(room)

    def charge(self, money):
        self.till += money

    def add_guest(self, guest):
        for room in self.booths:
            if len(room.guests) < room.capacity:
             room.guests.append(guest)
             break
        return "Sorry we are at max capacity"