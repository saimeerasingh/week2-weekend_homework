import unittest
from unittest.mock import patch

from src.songs import Songs
from src.guests import Guests

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

    def test_room_has_guest_list(self):
        self.assertEqual(0,len(self.room.guest_lists))
    
    def test_can_add_song_to_list(self):
        song = Songs('You are beautiful')
        self.room.add_song_to_list(song)
        self.assertEqual(4,len(self.room.songs))

    def test_can_remove_song_from_list(self):
        song = self.song1
        self.room.remove_song_from_list(song)
        self.assertEqual(2,len(self.room.songs))

    def test_can_add_money_to_till(self):
        self.room.add_money_to_till(15.50)
        self.assertEqual(266, self.room.till)
    
    def test_can_add_guest_to_list(self):
        guest = Guests('Eve',50,'Closer')
        self.room.guest_check_in(guest)
        self.assertEqual(1,len(self.room.guest_lists))

    def test_can_remove_guest_from_list(self):
        guest = Guests('Eve',50,'Closer')
        self.room.guest_check_in(guest)
        self.room.guest_check_out(guest)

    def test_can_check_room_capcity(self):
        capcity = self.room.room_capcity_check()
        self.assertLessEqual(0, capcity )

# Extensions solution:

    def test_if_more_guests_can_check_in(self):
        guest = Guests('Eve',50,'Closer')
        self.room.room_capcity_check()
        self.room.guest_check_in(guest)
        self.assertEqual(1, len(self.room.guest_lists))

    @patch('random.choice')
    def test_can_play_random_song_from_list(self,mock_choice):
        mock_choice.return_value = 'Closer'
        song_played = self.room.play_random_song()
        self.assertEqual('Closer' , song_played)
    
    def test_if_guests_can_cheer_for_favourite_song(self):
        guest1 = Guests('Eve',50,'Closer')
        guest2 = Guests('Ada',60,'Love Song')
        guest3 = Guests('Krish',75,'Sunshine')
        self.room.guest_check_in(guest1)
        self.room.guest_check_in(guest2)
        self.room.guest_check_in(guest3)
        return_value = self.room.guest_cheering()
        self.assertEqual('Whooo!', return_value)
    
    
        
        


       



        
