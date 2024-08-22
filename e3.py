# EX3
# Verifique uma condição para saber se o usuário é maior de idade.
 
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade")
elif idade == 0:
    print("idade inválida")
else:
    print("Você é menor de idade")