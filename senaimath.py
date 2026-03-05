def numero_e(termo):
    soma = 0
    fat = 1 # fatorial tem que ser difrente de 0

    #fatorial
    for n in range(termo):
        if n >0:
            fat *= n
        soma += 1/fat
    return soma

