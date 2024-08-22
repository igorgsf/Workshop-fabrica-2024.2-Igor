# Nesse caso, tentarei fazer algum pensamento abstrato em que eu possa criar uma solução problema com condicionais e repetições
# Decidi que meu caso de uso será para calcular descontos na mensalidade para ingressantes na faculdade

while True:

    print("------------- Bem vindo ao sistema de matricula unipê -------------")
    nome = input("Digite seu nome: ")
    curso = input("Digite seu curso pretendido: ")
    p1 = input("Você já é aluno unipê? (sim/não) : ").strip().lower()
    p2 = input("Você vem de outra instituição? (sim/não) : ").strip().lower()
    mensalidade = 1000

    if p1 == 'sim':
        print("Legal te ter aqui de volta, " + nome + ", você terá 30% de desconto na sua mensalidade, que será o valor de: R$" + str(mensalidade*0.7) + " reais")
        
    elif p2 == 'sim':
        print("Legal que tenha nos escolhido para fazer parte da sua jornada de ensino, " + nome + ", por isso, você terá 35% de desconto em sua mensalidade, que será: R$" + str(mensalidade*0.65) + " reais")

    else:
        print("Que bom que nos escolheu! " +  nome + ", você terá 15% de desconto em sua mensalidade, que será: R$ " + str(mensalidade*0.85) + " reais")
    
    resposta = input("Você deseja calcular outro valor? (sim/não) ").strip().lower() 
  

    if resposta == 'não':
        print("Esperamos ter ajudado, " + nome + "!")
        break

    print("Ok, vamos continuar!")
        
# Quais as condições? 
# Se já for aluno, automaticamente terá 30% de desconto
# Se for novato, terá 15% de desconto
# Se vier de outra instituição, terá 35% de desconto
