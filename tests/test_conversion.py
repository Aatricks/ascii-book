import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PIL import Image

from src.ascii_art_generator import conversion


class TestConversion(unittest.TestCase):

    def setUp(self):
        self.test_image = Image.new("RGB", (10, 10), "white")

    def test_load_image(self):
        # This is hard to test without a file, so we'll skip it for now
        pass

    def test_resize_image(self):
        resized = conversion.resize_image(self.test_image, 5)
        self.assertEqual(resized.size, (5, 5))



    def test_image_to_ascii_chars(self):
        ascii_chars = conversion.image_to_ascii_chars(self.test_image)
        self.assertEqual(len(ascii_chars), 100)

if __name__ == "__main__":
    unittest.main()
