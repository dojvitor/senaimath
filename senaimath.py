def fatorial(numero):
    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor


def pi(n=10000000):
    c = 0
    for i in range (n):
        a = (-1)**i
        b = (2*i)+1
        c += a/b
    resultado = 4*(c)
    return resultado