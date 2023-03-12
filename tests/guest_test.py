import unittest
from src.guest import Guest
from src.caraoke_bar import CaraokeBar

class TestGuest(unittest.TestCase):
   
   def setUp(self):
       self.guest = Guest("Terry", "Mambo No. 5",10)
       self.bar = CaraokeBar("CCC", 100, 5)


   def test_check_guest_name(self):
       self.assertEqual("Terry", self.guest.name)

   def test_pay(self):
       self.guest.pay(self.bar.entry_fee)
       self.assertEqual(5, self.guest.wallet)