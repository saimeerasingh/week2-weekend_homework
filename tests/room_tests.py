import unittest
from songs import Songs

from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Songs('Closer')
        self.song2 = Songs('Sunshine')
        self.song3 = Songs('Love Song')
        self.songs = [self.song1,self.song2,self.song3]

        self.room = Room('Radio Star',250.50,20,self.songs)
        
