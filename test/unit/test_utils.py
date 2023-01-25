import unittest

from app.utils import to_fixed


class TestUtils(unittest.TestCase):

    def test_to_fixed(self):
        self.assertEqual(to_fixed(20.343), 20.34)
        self.assertEqual(to_fixed(1.3), 1.3)
        self.assertEqual(to_fixed(204.3133567), 204.31)