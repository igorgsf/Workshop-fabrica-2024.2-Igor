# EX1
# Peça para o usuário digitar um número
# Verifique se o número é maior que 50 e imprima na tela "O número X é maior que 50"

numero = int(input("Digite um número: "))

if numero > 50:
    print("O número " + str(numero) + " é maior que 50")
elif numero == 50:
    print("o número é exatamente " + str (numero))
else:
    print("O número " + str(numero) + " é menor que 50")
