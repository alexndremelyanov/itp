import unittest
from unittest.mock import patch, call
from decorator_ import separated_print


@separated_print
def hello():
    print('Hello')


class Test(unittest.TestCase):
    @patch('builtins.print')
    def test(self, mock_print):
        hello()
        self.assertEqual(mock_print.mock_calls, [call(
            '--------------'), call('Hello'), call('--------------')])
        # hello("Hello")
        # print(mock_print.mock_calls)
        # self.assertEqual(mock_print)
