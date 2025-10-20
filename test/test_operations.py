from src.add_fun import add, sub, ret


def test_add():
    assert add(2, 3) == 5
    assert add(3, 3) == 6
    assert add(8, 2) == 10
    assert add(3, 7) == 10
    assert add(3, 3) == 6


def test_sub():
    assert sub(6, 2) == 4
    assert sub(3, 3) == 0


def test_ret():
    assert ret("sayjvsf") == "sayjvsf"
    assert ret("kdshcvd") == "kdshcvd"
    assert ret("sayjvsf") == "sayjvsf"
    assert ret("sayjvsf") == "sayjvsf"
    assert ret("sayjvsf") == "sayjvsf"
