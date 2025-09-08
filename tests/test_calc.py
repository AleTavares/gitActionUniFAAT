from app.calc import soma, multiplica
from app.calc import potencia  # Importing the potencia function

def test_potencia():
    assert potencia(2, 3) == 8  # corrigido para o valor correto
    assert potencia(5, 0) == 1
    assert potencia(3, 2) == 9
def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6