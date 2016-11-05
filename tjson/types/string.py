from tjson import ParseError


def parse(value):
    if ':s' not in value:
        raise ParseError

    return value.split(':s')[0]
