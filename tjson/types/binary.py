from base64 import b16decode, b32decode, b64decode
from tjson import ParseError  # noqa


def _fix_b32_padding(value):
    missing_padding = len(value) % 8
    if missing_padding:
        return '{}{}'.format(value, '=' * (8 - missing_padding))
    return value


def _fix_b64_padding(value):
    return value + '==='


def parse_b16(value):
    if ":b16" not in value:
        return b16decode(value.upper()).decode()
    return b16decode(value.split(':b16')[0].upper()).decode()


def parse_b32(value):
    if ":b32" in value:
        value = value.split(':b32')

    value = _fix_b32_padding(value)
    return b32decode(value, True).decode()


def parse_b64(value):
    if ":b64" in value:
        value = value.split(':b64')

    value = _fix_b64_padding(value)
    return b64decode(value).decode()
