from integersums import add_it_up


def test_to_ten():
    results = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    for n in range(10):
        assert add_it_up(n) == results[n]


def test_string():
    assert add_it_up("testing") == 0


def test_float():
    assert add_it_up(0.124) == 0


def test_negative():
    assert add_it_up(-19) == 0