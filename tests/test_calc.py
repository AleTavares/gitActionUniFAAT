from app.calc import soma, multiplica
#teste
def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divisao():
    assert divisao(10, 2) == 5

def test_minus():
    assert minus(4, 2) == 2