from app.calc import soma, multiplica

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divide():
    assert potencia(4, 2) == 2

def test_subtração():
    assert subtração(3, 1) == 2