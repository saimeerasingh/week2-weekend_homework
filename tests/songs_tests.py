import unittest

from src.songs import Songs
class TestSongs(unittest.TestCase):
    def setUp(self):
        self.song1 = Songs('Closer')
        self.song2 = Songs('Sunshine')
        self.song3 = Songs('Love Song')