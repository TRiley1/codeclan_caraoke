import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestRoom(unittest.TestCase):
   def setUp(self):
       self.room = Room(1)
       self.song = Song("Jailhouse Rock", "Elvis", "Rock")
       self.song2 = Song("Still into You", "Paramore", "Punk Rock")
       self.guest = Guest("Terry", "Mambo No. 5")

   def test_room_id(self):
       self.assertEqual(1, self.room.id)

   def test_song_artist(self):
       self.assertEqual("Elvis", self.song.artist)

   def test_add_guest_to_room(self):
       self.room.add_guest(self.guest.name)
       self.assertEqual(["Terry"], self.room.guests)

   def test_remove_guest_from_room(self):
       self.room.add_guest(self.guest.name)
       self.room.remove_guest(self.guest.name)
       self.assertEqual([], self.room.guests)

   def test_add_song_to_track_list(self):
       self.room.add_song(self.song)
       self.assertEqual([self.song], self.room.track_list)

   def test_add_two_songs_to_track_list(self):
       self.room.add_song(self.song)
       self.room.add_song(self.song2)
       self.assertEqual([self.song,self.song2], self.room.track_list)