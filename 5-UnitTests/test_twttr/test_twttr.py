from twttr import shorten


def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("hihi") == "hh"
    assert shorten("hi hello") == "h hll"
    assert shorten("aeiou") == ""
