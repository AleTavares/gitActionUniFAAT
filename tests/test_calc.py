from app.calc import soma, multiplica
from app.calc import potencia

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6
def test_potencia():
    assert potencia(2, 3) == 9  # valor errado propositalmente
    assert potencia(5, 0) == 1
    assert potencia(3, 2) == 9