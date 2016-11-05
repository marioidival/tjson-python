from unittest import TestCase
from tjson import parse


class TestTJsonParse(TestCase):

    def test_parse_utf8_string(self):
        expected = {'foo': 'bar'}
        result = parse('{"s:foo": "s:bar"}')

        self.assertEqual(expected, result)
