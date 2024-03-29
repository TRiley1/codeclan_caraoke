import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 
from src.caraoke_bar import CaraokeBar

class TestRoom(unittest.TestCase):
   def setUp(self):
       self.room = Room(1,4)
       self.song = Song("Jailhouse Rock", "Elvis", "Rock")
       self.song2 = Song("Still into You", "Paramore", "Punk Rock")
       self.guest = Guest("Terry", "Mambo No. 5", 7)
       self.bar = CaraokeBar("CCC",100,5)

   def test_room_id(self):
       self.assertEqual(1, self.room.id)

#    def test_max_capacity(self):
#        self.room.add_guest(self.guest)
#        self.room.add_guest(self.guest)
#        self.room.add_guest(self.guest)
#        self.room.add_guest(self.guest)
#        result = self.room.add_guest(self.guest)
#        self.assertEqual("Capacity Full", result)

   def test_song_artist(self):
       self.assertEqual("Elvis", self.song.artist)

   def test_if_fav_song_on_track_list(self):
       self.bar.add_room_to_booth(self.room)
       self.bar.add_guest(self.guest)
       self.room.add_song(self.guest.fav_song)
       result = self.room.check_fav()
       self.assertEqual("Yipee!", result)

   def test_add_fav_if_not_there(self):
        self.bar.add_room_to_booth(self.room)
        self.bar.add_guest(self.guest)
        self.room.check_fav()
        self.assertEqual(1, len(self.room.track_list))

#    def test_add_guest_to_room(self):
#        self.room.add_guest(self.guest.name)
#        self.assertEqual(["Terry"], self.room.guests)

   def test_add_snack(self):
       self.room.add_snack("Crisps", "£1")
       self.assertEqual({"Crisps" : "£1"}, self.room.snacks)

   def test_sell_snacks(self):
       self.room.add_snack("Crisps", 1)
       self.room.sell_snack("Crisps")
       self.assertEqual(1, self.room.tab)
       

   def test_remove_guest_from_room(self):
       self.bar.add_room_to_booth(self.room)
       self.bar.add_guest(self.guest.name)
       self.room.remove_guest(self.guest.name)
       self.assertEqual([], self.room.guests)

   def test_add_song_to_track_list(self):
       self.room.add_song(self.song)
       self.assertEqual([self.song], self.room.track_list)

   def test_add_two_songs_to_track_list(self):
       self.room.add_song(self.song)
       self.room.add_song(self.song2)
       self.assertEqual([self.song,self.song2], self.room.track_list)