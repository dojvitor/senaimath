def fatorial(numero):
    if numero == 0:
        return 1
    valor = numero
    for _ in range(1, numero):
        valor *= numero - 1
        numero -= 1
    return valor

def ang_radiano(angulo):
    radiano = angulo * 3.1415 / 180
    return radiano

def cosseno(grau, termos):
    radiano = ang_radiano(grau)
    cosseno = 0
    
    for n in range(termos):
        sinal_formula = (-1)**n
        numerador = radiano**(2*n)
        denominador = fatorial(2*n)
        termos = sinal_formula * (numerador / denominador)
        cosseno += termos
    return cosseno

def seno(x, termos=10):
    soma = 0
    for n in range(termos):
        numerador = (-1)**n * x**(2*n + 1)
        denominador = fatorial(2*n + 1)
        soma += numerador / denominador
    return soma


while True:
    try:
        angulo = float(input("Digite o ângulo em graus: "))
        
        rad = ang_radiano(angulo)
        resultado = seno(rad)

        print(f"\nO seno de {angulo}° é aproximadamente: {resultado:.6f}\n")

        opcao = input("Deseja calcular outro ângulo? (s/n): ").lower()
        if opcao != 's':
            print("Programa encerrado.")
            break

    except ValueError:
        print("Por favor, digite um número válido.\n")
