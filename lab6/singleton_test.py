import unittest
from singleton import Singleton


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Singleton(), Singleton())
