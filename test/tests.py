import unittest
from src.image_handling import *
from src.image_encoding import *
from src.encoding import *


class test_decoding(unittest.TestCase):
    def test_decode_image(self):
        test_image, image_type = load_image('../figures/encoded_github.png')
        decoded_text = decode_image(test_image, image_type=image_type)
        self.assertEqual(decoded_text[0:9], 'Nel mezzo')


class test_encoding(unittest.TestCase):
    def test_encoding(self):
        encoded_char = get_encoding('A', color_step=0.5, base=6)
        self.assertEqual(encoded_char, [-1., 0.5, 1.])


if __name__ == '__main__':
    unittest.main()
