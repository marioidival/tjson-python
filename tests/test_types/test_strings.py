from unittest import TestCase
from tjson import ParseError
from tjson.types.string import parse


class TestTypeString(TestCase):

    def test_utf8_string(self):
        expected = 'hello, world!'
        result = parse('hello, world!:s')

        self.assertEqual(expected, result)

    def test_untagged_string(self):
        with self.assertRaises(ParseError):
            result = parse('hello, world!')  # noqa
