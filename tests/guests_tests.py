import unittest

from src.room import Room
from src.guests import Guests
from src.songs import Songs

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guests('Eve',50,'Closer')
        self.guest2 = Guests('Ada',60,'Love Song')
        self.guest3 = Guests('Krish',75,'Sunshine')
        self.guest_list = [self.guest1,self.guest2,self.guest3]
        self.songs = [Songs('Closer'), Songs('Sunshine'),Songs('Love Song')]
    
    
    def test_check_guest_has_name(self):
        self.assertEqual('Eve',self.guest1.name)

    def test_check_guest_has_wallet(self):
        self.assertEqual(60 , self.guest2.wallet)

    def test_check_guest_has_favourite_song(self):
        self.assertEqual('Sunshine' , self.guest3.favourite_song)

  

        