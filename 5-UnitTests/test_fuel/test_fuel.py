from fuel import convert, gauge


def test_guage():
    assert gauge(100) == "F"
    assert gauge(50) == 50


def test_convert():
    assert convert("1/2") == 50
    assert convert("3/2") is None
    assert convert("cat") is None
