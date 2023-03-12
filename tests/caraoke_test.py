import unittest
from src.caraoke_bar import CaraokeBar
from src.room import Room
from src.guest import Guest

class TestCaraokeBar(unittest.TestCase):
    def setUp(self):
        self.caraoke_bar = CaraokeBar("CCC", 100, 5)
        self.room = Room(1, 1)
        self.room2 = Room(2, 4)
        self.room3 = Room(3,4)
        self.guest = Guest("Tam", "Send me your location",10)

    def test_add_room_to_booth(self):
        self.caraoke_bar.add_room_to_booth(self.room)
        self.assertEqual([self.room], self.caraoke_bar.booths)

    def test_add_guests_to_room(self):
        self.caraoke_bar.add_room_to_booth(self.room)
        self.caraoke_bar.add_room_to_booth(self.room2)
        self.caraoke_bar.add_room_to_booth(self.room3)
        self.caraoke_bar.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_add_money_to_till(self):
        self.caraoke_bar.charge(self.caraoke_bar.entry_fee)
        self.assertEqual(105 , self.caraoke_bar.till)

    def test_add_two_guests_to_room(self):
        self.guest2 = Guest("Del", "Lookers Street",12)
        self.caraoke_bar.add_room_to_booth(self.room)
        self.caraoke_bar.add_room_to_booth(self.room2)
        self.caraoke_bar.add_room_to_booth(self.room3)
        self.caraoke_bar.add_guest(self.guest)
        self.caraoke_bar.add_guest(self.guest2)
        self.assertEqual(1, len(self.room2.guests))

    def test_max_capacity(self):
        self.room4 = Room(4,0)
        self.caraoke_bar.add_room_to_booth(self.room4)
        result = self.caraoke_bar.add_guest(self.guest)
        self.assertEqual("Sorry we are at max capacity", result)
