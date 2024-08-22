#Ex4 Faça uma lógica que faça sentido
#Menor de 16 = não pode voltar
#Entre 16 e 17 ou 70+ anos = voto opcional
# Entre 18 e 69 anos = voto obrigatório

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <70:
    print("Seu voto é obrigatório")
elif idade >= 16 or idade >= 70:
    print("Seu voto é optativo, você decide!")
else:
    print("Seu voto não é obrigatório")