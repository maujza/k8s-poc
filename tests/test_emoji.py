import os
import unittest
from requests import get

from simple_app.app.utils.get_emojis import get_smile_emoji

class EmojiCharTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.URL = "https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json"
        cls.test_path = "./simple_app/app/utils/emoji.json"
        cls.fetch_and_write_emoji_json(cls.URL, cls.test_path)

    @classmethod
    def fetch_and_write_emoji_json(cls, url, path):
        response = get(url)
        with open(path, "w") as file:
            file.write(response.text)

    def setUp(self):
        self.emoji = get_smile_emoji(self.test_path)

    def test_char(self):
        self.assertEqual("😄", self.emoji)


if __name__ == "__main__":
    unittest.main()
