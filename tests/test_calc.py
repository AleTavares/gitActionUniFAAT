from app.calc import soma, multiplica, divisao, subtracao, potencia

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(3, 2) == 1

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divisao():
    assert divisao(6, 2) == 3

def test_potencia():
    assert potencia(2, 3) == 8  # 2³ = 8
    assert potencia(3, 2) == 9  # 3² = 9
    assert potencia(5, 0) == 1  # qualquer número elevado a 0 é 1
