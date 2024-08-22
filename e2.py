# EX2
# Peça ao usuário para digitar um número
# Verifique se é par ou impar

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número " + str(numero) + " é par")
else:
    print("O número " + str(numero) + " é impar")