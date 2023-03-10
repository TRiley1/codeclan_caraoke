import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song 

class TestRoom(unittest.TestCase):
   
   def setUp(self):
       self.room = Room(1)
       self.song = Song("Jailhouse Rock", "Elvis", "Rock")
       self.guest = Guest("Terry")

   def test_room_id(self):
       self.assertEqual(1, self.room.id)

   def test_song_artist(self):
       self.assertEqual("Elvis", self.song.artist)