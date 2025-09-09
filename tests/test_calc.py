from app.calc import soma, multiplica, divide, subtração

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divide():
    assert divide(4, 2) == 2

def test_subtração():
    assert subtração(4, 1) == 3