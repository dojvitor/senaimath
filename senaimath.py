def fatorial(numero):
    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor