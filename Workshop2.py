continuar = 1

while continuar == 1:
    nota1 = float(input("Digite sua primeira nota: "))

    nota2 = float(input("Digite sua segunda nota: "))

    soma = nota1 + nota2
    media = soma/2

    if media  <= 6 and media > 0 :
        print(f"Estude mais você foi reprovado, sua media foi: {media}")

    elif media >= 7 and media <9:
        print(f"Parabens você foi aprovado, sua media foi: {media}")

    else:
        print(f"Media excelente, você tirou: {media}")

    continuar = int(input("Você quer continuar? [0]Não [1]Sim"))

if continuar == 0 and media > 6:
 print("Parabens, volte sempre! ")

elif continuar == 0 and media < 6:
   print("Estude mais e volte sempre!")