from app.calc import soma, multiplica, divisao, subtracao, potenciacao

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(5, 2) == 3

def test_multiplica():
    assert multiplica(4, 3) == 12

def test_divisao():
    assert divisao(6, 2) == 3

def test_potenciacao():
    assert 2 ** 3 == 8
