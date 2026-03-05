def fatorial(numero):
    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor

# log natural
x = float(input("de um valor a X"))
k = 100
def log_natural(x, k=100):
    if x <= 0:
        return "erro x deve ser maior que 0"

soma = 0
t_b = (x - 1) / (x + 1)

for i in range(k + 1):
    d = 2 * i + 1
    pot = t_b **(2 * i + 1)
    soma += (1 / d) * pot
    resultado =  2 * soma

print(resultado)