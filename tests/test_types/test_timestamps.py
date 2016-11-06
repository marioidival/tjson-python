from unittest import TestCase, skip
from datetime import datetime
from tjson.types.timestamp import parse_timestamp


class TestTimestamps(TestCase):
    
    @skip('Not working yet')
    def test_timestamp_valid(self):
        result = parse_timestamp('2016-10-02T07:31:51Z')

        self.assertIsInstance(result, datetime)
