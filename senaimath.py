import math

def exponencial_auto(x):
    if x < 0:
        return 1 / exponencial_auto(abs(x))
    
    
    termos = int(2 * x + 20)
    
    soma = 1.0
    termo_atual = 1.0  
    
    for n in range(1, termos):
        termo_atual *= (x / n)
        soma += termo_atual
        
        if termo_atual < 1e-18: 
            break
            
    return soma

try:
    x_input = input("Digite o valor de X: ")
    x = float(x_input)
    
    meu_resultado = exponencial_auto(x)
    resultado_real = math.exp(x) 

    print(f" Resultados para x = {x} ")
    print(f"Série de Taylor: {meu_resultado:.15f}")
    print(f"Diferença:       {abs(meu_resultado - resultado_real):.2e}")

except ValueError:
    print("Erro: Por favor, digite um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero (provavelmente x muito grande negativo).")
def numero_e(termo):
    soma = 0
    fat = 1 # fatorial tem que ser difrente de 0

    #fatorial
    for n in range(termo):
        if n >0:
            fat *= n
        soma += 1/fat # numero será divifido pelo fatorial

    return soma

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
