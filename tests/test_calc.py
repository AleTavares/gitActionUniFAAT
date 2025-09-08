from app.calc import soma, multiplica, divide, subtrai

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    assert multiplica(2, 3) == 6

def test_divide():
    assert divide(4, 2) == 2

def test_subtrai():
    assert subtrai(6, 3) == 3      