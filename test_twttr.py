from twttr import shorten


def test_lowercase():
    assert shorten("text") == "txt"
