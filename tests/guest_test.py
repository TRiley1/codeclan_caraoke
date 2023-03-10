import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
   
   def setUp(self):
       self.guest = Guest("Terry")

   def test_check_guest_name(self):
       self.assertEqual("Terry", self.guest.name)