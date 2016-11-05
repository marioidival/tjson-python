from tjson import ParseError


SIGNED_MAXINT = 9223372036854775807
SIGNED_MININT = -922337203685477508
UNSIGNED_MAXINT = 18446744073709551615


def parse_signed_int(value):
    value = int(value, 10)
    if value > SIGNED_MAXINT or value < SIGNED_MININT:
        raise ParseError
    return value


def parse_unsigned_int(value):
    value = int(value, 10)
    if value < 0 or value > UNSIGNED_MAXINT:
        raise ParseError

    return value
