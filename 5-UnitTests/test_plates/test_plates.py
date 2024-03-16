from plates import is_valid


def test_plates():
    assert is_valid("CS50")


def test_length():
    assert not is_valid("H")


def test_symbols():
    assert not is_valid("PI3.14")


def test_num():
    assert not is_valid("CS05")
