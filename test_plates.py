from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") is True
    assert is_valid("HI") is True
