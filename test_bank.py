from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, Newman") == 0
