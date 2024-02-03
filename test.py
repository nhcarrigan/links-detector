"""Tests to validate that the pattern behaves as expected."""
import re
import unittest

from pattern import LINKS, PATTERN


class TestPattern(unittest.TestCase):
    """Tests for the link pattern."""

    def test_twitch(self):
        """Tests against twitch links."""
        self.assertTrue(re.search(PATTERN, "https://twitch.tv/naomilgbt"))
        self.assertTrue(re.search(PATTERN, "http://twitch.tv/naomilgbt"))
        self.assertFalse(re.search(PATTERN, "https://twitch.tv"))
        self.assertFalse(re.search(PATTERN, "https://twitch.tv/"))
        self.assertTrue(
            re.search(PATTERN, "Streaming now!\nhttps://twitch.tv/naomilgbt\nCome join?"))
        self.assertTrue(re.search(PATTERN, "<https://twitch.tv/naomilgbt>"))
        self.assertFalse(
            re.search(PATTERN, "Streaming now!\nhttps://twitch.tv/\nCome join?"))

    def test_kick(self):
        """Tests against kick links."""
        self.assertTrue(re.search(PATTERN, "https://kick.com/naomilgbt"))
        self.assertFalse(re.search(PATTERN, "https://kick.com"))
        self.assertFalse(re.search(PATTERN, "https://kick.com/"))
        self.assertTrue(
            re.search(PATTERN, "Streaming now!\nhttps://kick.com/naomilgbt\nCome join?"))
        self.assertTrue(re.search(PATTERN, "<https://kick.com/naomilgbt>"))
        self.assertFalse(
            re.search(PATTERN, "Streaming now!\nhttps://kick.com/\nCome join?"))

    def test_random(self):
        """Tests against invalid links."""
        self.assertFalse(re.search(PATTERN, "https://naomi.lgbt"))
        self.assertFalse(re.search(PATTERN, "https://streamcord.io"))

    def test_links(self):
        """Tests against all links."""
        self.assertTrue(re.search(PATTERN, "https://kick.com/naomilgbt"))
        self.assertFalse(re.search(PATTERN, "https://kick.com"))
        self.assertFalse(re.search(PATTERN, "https://kick.com/"))
        self.assertTrue(
            re.search(PATTERN, "Streaming now!\nhttps://kick.com/naomilgbt\nCome join?"))
        self.assertTrue(re.search(PATTERN, "<https://kick.com/naomilgbt>"))
        self.assertFalse(
            re.search(PATTERN, "Streaming now!\nhttps://kick.com/\nCome join?"))
        self.assertTrue(re.search(PATTERN, "https://twitch.tv/naomilgbt"))
        self.assertTrue(re.search(PATTERN, "http://twitch.tv/naomilgbt"))
        self.assertFalse(re.search(PATTERN, "https://twitch.tv"))
        self.assertFalse(re.search(PATTERN, "https://twitch.tv/"))
        self.assertTrue(
            re.search(PATTERN, "Streaming now!\nhttps://twitch.tv/naomilgbt\nCome join?"))
        self.assertTrue(re.search(PATTERN, "<https://twitch.tv/naomilgbt>"))
        self.assertFalse(
            re.search(PATTERN, "Streaming now!\nhttps://twitch.tv/\nCome join?"))
        self.assertFalse(re.search(PATTERN, "https://naomi.lgbt"))
        self.assertFalse(re.search(PATTERN, "https://streamcord.io"))

    def test_multiple_links(self):
        """Tests comparisons of messages with multiple links."""
        self.assertEqual(len(re.findall(PATTERN, "https://twitch.tv/naomilgbt")),
                         len(re.findall(LINKS, "https://twitch.tv/naomilgbt")))
        self.assertEqual(len(re.findall(PATTERN, "https://kick.com/naomilgbt")),
                         len(re.findall(LINKS, "https://kick.com/naomilgbt")))
        self.assertLess(len(re.findall(PATTERN, "https://naomi.lgbt")),
                        len(re.findall(LINKS, "https://naomi.lgbt")))
        self.assertLess(
            len(re.findall(PATTERN, "https://twitch.tv/naomilgbt\nhttps://chat.naomi.lgbt")),
            len(re.findall(LINKS, "https://twitch.tv/naomilgbt\nhttps://chat.naomi.lgbt")))
        self.assertLess(
            len(re.findall(
                PATTERN, "https://twitch.tv/naomilgbt" +
                "\nhttps://chat.naomi.lgbt\nhttps://kick.com/naomilgbt")),
            len(re.findall(LINKS, "https://twitch.tv/naomilgbt" +
                "\nhttps://chat.naomi.lgbt\nhttps://kick.com/naomilgbt")))


unittest.main()
