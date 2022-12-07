import unittest
from unittest.mock import patch, call
from factory import Factory


class Test(unittest.TestCase):
    @patch('builtins.print')
    def test(self, mock_print):
        for type in ["button", "container", "audio"]:
            element = Factory.create_element(type)
            print(element.get_html())

        self.assertEqual(mock_print.mock_calls, [
            call('<button></button>'),
            call('<div></div>'),
            call('<audio />')
        ])
