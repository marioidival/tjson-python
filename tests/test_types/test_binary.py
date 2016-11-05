from unittest import TestCase
from tjson.types.binary import parse_b16
from tjson.types.binary import parse_b32
from tjson.types.binary import parse_b64


class TestBinary(TestCase):

    def test_valid_base16(self):
        expected = 'Hello, world!'
        result = parse_b16('48656c6c6f2c20776f726c6421')

        self.assertEqual(expected, result)

    def test_valid_base32(self):
        expected = 'Hello, world!'
        result = parse_b32('jbswy3dpfqqho33snrscc')

        self.assertEqual(expected, result)

    def test_valid_base64(self):
        expected = 'Hello, world!'
        result = parse_b64('SGVsbG8sIHdvcmxkIQ')

        self.assertEqual(expected, result)
