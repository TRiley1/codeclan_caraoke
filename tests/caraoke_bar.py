import unittest
from caraoke_bar import CaraokeBar

class TestCaraokeBar(unittest.TestCase):
    def setUp(self):
        self.caraoke_bar = CaraokeBar("CCC", 100, 5)