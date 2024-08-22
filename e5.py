# EX5 - DESCONTO EM COMPRA

while True:

    valor = float(input("Qual valor da compra? "))

    if valor >= 500:
        print("Você ganhou 20% de desconto. O valor da sua compra com o desconto é: R$ " + str(valor*0.8))
    elif valor >= 250:
        print("Você ganhou 10% de desconto. O valor da sua compra com desconto é: R$ " + str(valor*0.9))
    else:
        print("Você não ganou nenhum desconto. O valor da sua compra é: R$ "+ str(valor))

    # Perguntar ao usuário se ele gostaria de calcular outro valor
    
    resposta = input("Você deseja calcular outro valor? (sim/não) ").strip().lower() 
    #Strip remove os espaços em branco extras no início e no final da string.
    #lower Converte todos os caracteres da string para minúsculas.

    if resposta == 'não':
        break

    print("Ok, vamos continuar!")
