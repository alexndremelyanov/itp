import unittest
from decorator_ import List, JSON


class Test(unittest.TestCase):
    def test(self):
        list = List(['first', 'second'])
        json = JSON(['parent', {'child': 1}])
        self.assertEqual(str(list), 'first second')
        self.assertEqual(str(json), '["parent", {"child": 1}]')
