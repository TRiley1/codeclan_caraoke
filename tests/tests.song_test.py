import unittest
from src.song import Song

class TestSong(unittest.TestCase):
   
   def setUp(self):
      self.song = Song("Jailhouse Rock", "Elvis", "Rock")
