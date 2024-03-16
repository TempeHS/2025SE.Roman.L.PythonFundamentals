from bank import value


def test_value():
    assert value("hello") == "$0"
    assert value("Hello") != "$0"
    assert value("hi") == "$20"
    assert value("yo") == "$100"


# capitals are converted to lower before function is called


# numbers and symbols are still counted as greetings on purpose
def test_number():
    assert value("1") == "$100"


def test_symbol():
    assert value("?") == "$100"
