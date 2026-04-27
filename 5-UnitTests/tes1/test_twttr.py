from twttr import shorten


def test_Lowercase():
    assert shorten("text") == "txt"
