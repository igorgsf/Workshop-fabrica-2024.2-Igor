def menor_valor(valor1, valor2):
    if valor1 < valor2:
        return valor1
    return valor2

def menor_valor2(valor1, valor2, valor3):
    return menor_valor(valor3, menor_valor(valor1, valor2))

print(f'O menor valor é: {menor_valor2(123,321,456)}')
