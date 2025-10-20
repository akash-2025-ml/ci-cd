from src.add_fun import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(3, 3) == 6


def test_sub():
    assert sub(6, 2) == 4
    assert sub(3, 3) == 0
