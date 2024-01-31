import unittest
import re
from pattern import pattern

class TestPattern(unittest.TestCase):
    def test_twitch(self):
        self.assertTrue(re.search(pattern, "https://twitch.tv/naomilgbt"))
        self.assertTrue(re.search(pattern, "http://twitch.tv/naomilgbt"))
        self.assertFalse(re.search(pattern, "https://twitch.tv"))
        self.assertFalse(re.search(pattern, "https://twitch.tv/"))
        self.assertTrue(re.search(pattern, "Streaming now!\nhttps://twitch.tv/naomilgbt\nCome join?"))
        self.assertTrue(re.search(pattern, "<https://twitch.tv/naomilgbt>"))
        self.assertFalse(re.search(pattern, "Streaming now!\nhttps://twitch.tv/\nCome join?"))

    def test_kick(self):
        self.assertTrue(re.search(pattern, "https://kick.com/naomilgbt"))
        self.assertFalse(re.search(pattern, "https://kick.com"))
        self.assertFalse(re.search(pattern, "https://kick.com/"))
        self.assertTrue(re.search(pattern, "Streaming now!\nhttps://kick.com/naomilgbt\nCome join?"))
        self.assertTrue(re.search(pattern, "<https://kick.com/naomilgbt>"))
        self.assertFalse(re.search(pattern, "Streaming now!\nhttps://kick.com/\nCome join?"))

    def test_random(self):
        self.assertFalse(re.search(pattern, "https://naomi.lgbt"))
        self.assertFalse(re.search(pattern, "https://streamcord.io"))

unittest.main()