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