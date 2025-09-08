from app.calc import soma, multiplica, subtracao, divisao

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_subtracao():
    assert subtracao(2, 2) == 0

def test_divisao():
    assert divisao(6, 2) == 3

def test_divisao_por_zero():
    try:
        divisao(5, 0)
        assert False, "Deveria ter levantado ValueError"
    except ValueError:
        assert True