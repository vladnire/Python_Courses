from caesar import caesar


def test_a():
    assert caesar("aaa", 1) == "bbb"
    assert caesar("aaa", 5) == "fff"


def test_punctuation():
    assert caesar("aaa.bbb", 1) == "bbb.ccc"
    assert caesar("aaa.bbb", -1) == "zzz.aaa"


def test_whitespace():
    assert caesar("aaa    bb b", 1) == "bbb    cc c"
    assert caesar("aaa    bb b", 3) == "ddd    ee e"


def test_wraparound():
    assert caesar("abc", -1) == "zab"
    assert caesar("abc", -2) == "yza"
    assert caesar("abc", -3) == "xyz"

    assert caesar("xyz", 1) == "yza"
    assert caesar("xyz", 2) == "zab"
    assert caesar("xyz", 3) == "abc"