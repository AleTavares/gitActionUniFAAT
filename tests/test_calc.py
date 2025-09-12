from app.calc import soma, subtracao, multiplica, divisao, potencia, modulo, raiz_quadrada

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(3, 2) == 1

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divisao():
    assert divisao(6, 2) == 3

def test_potencia():
    assert potencia(2, 3) == 8

def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(10, 2) == 0  # teste extra

def test_raiz_quadrada():
    assert raiz_quadrada(16) == 4
    assert raiz_quadrada(25) == 5  # teste extra

