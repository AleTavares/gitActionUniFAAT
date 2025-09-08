def soma(a, b):
    # return a - b  # ERRO proposital
    return a + b  # Correção

def subtracao(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b
