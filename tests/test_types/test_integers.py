from unittest import TestCase
from tjson import ParseError
from tjson.types.integer import parse_signed_int
from tjson.types.integer import parse_unsigned_int


class TestInteger(TestCase):

    def test_signed_int(self):
        expected = 42
        result = parse_signed_int('42')

        self.assertEqual(expected, result)

        expected = -42
        result = parse_signed_int("-42")

        self.assertEqual(expected, result)

    def test_oversized_signed_int(self):
        test_value = str((2 ** 63))

        with self.assertRaises(ParseError):
            result = parse_signed_int(test_value)  # noqa

    def test_undersized_signed_int(self):
        test_value = str(-(2 ** 63) - 1)

        with self.assertRaises(ParseError):
            result = parse_signed_int(test_value)  # noqa

    def test_unsigned_int(self):
        expected = 0
        result = parse_unsigned_int('0')

        self.assertEqual(expected, result)

        expected = (2 ** 64) - 1
        result = parse_unsigned_int(str(expected))

        self.assertEqual(expected, result)

    def test_oversized_unsigned_int(self):
        test_value = (2 ** 64)
        with self.assertRaises(ParseError):
            result = parse_unsigned_int(str(test_value))  # noqa

    def test_udersized_unsigned_int(self):
        test_value = -1
        with self.assertRaises(ParseError):
            result = parse_unsigned_int(str(test_value))  # noqa
