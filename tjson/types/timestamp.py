from datetime import datetime

ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


def parse_timestamp(value):
    return datetime.strptime(value, ISO_FORMAT)
