import unittest
from unittest.mock import patch, call
from observer import Observer


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print('{} got message "{}"'.format(self.name, message))


class Test(unittest.TestCase):
    @patch('builtins.print')
    def test(self, mock_print):
        observer = Observer()
        sub_1 = Subscriber('First Sub')
        sub_2 = Subscriber('Second Sub')
        observer.register(sub_1)
        observer.register(sub_2)
        observer.dispatch("Hi")
        self.assertEqual(mock_print.mock_calls, [call(
            'First Sub got message "Hi"'), call('Second Sub got message "Hi"')])
        observer.unregister(sub_1)
        observer.dispatch('sub_1 is so nasty')
        self.assertEqual(mock_print.mock_calls, [call(
            'First Sub got message "Hi"'), call('Second Sub got message "Hi"'), call('Second Sub got message "sub_1 is so nasty"')])
        observer.register(sub_1)
        observer.dispatch('you also have problems with stack?')
        observer.unregister(sub_2)
        observer.unregister(sub_1)
