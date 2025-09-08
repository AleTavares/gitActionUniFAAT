from app.calc import soma, multiplica

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_potencia():
    assert potencia(3, 2) == 9