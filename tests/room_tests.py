import unittest

from src.songs import Songs

from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Songs('Closer')
        self.song2 = Songs('Sunshine')
        self.song3 = Songs('Love Song')
        self.songs = [self.song1,self.song2,self.song3]

        self.room = Room('Radio Star',250.50,15.50,20,self.songs)
        
    def test_room_has_name(self):
        self.assertEqual('Radio Star', self.room.name)

    def test_room_has_till(self):
        self.assertEqual(250.50,self.room.till)
    
    def test_room_has_ticket_price(self):
        self.assertEqual(15.50,self.room.ticket_price)
    
    def test_room_has_capcity(self):
        self.assertEqual(20,self.room.capcity)

    def test_room_has_songs_list(self):
        self.assertEqual(3,len(self.room.songs))

    
