import unittest

from src.guests import Guests

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guests('Eve',50,'Closer')
        self.guest2 = Guests('Ada',60,'Love Song')
        self.guest3 = Guests('Krish',75,'Sunshine')
    
    
        