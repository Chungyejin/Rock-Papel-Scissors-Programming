print("\n---| Jokenpô |---- \n1 - humano x humano \n2 - humano x computador \n3 - computador x computador \n")
modalidade = int(input("Escolha a modalidade: "))

##if modalidade != 1 or modalidade != 2 or modalidade != 3:
##print("\nModalidade inválida, tente novamente!")
##modalidade = int(input("\nEscolha a modalidade: "))

##modalidade 1 - humano x humano
if modalidade == 1:
  nome1 = input("\nDigite o nome do primeiro jogador: ")
  nome2 = input("Digite o nome do segundo jogador: ")
  print("\nOlá " + (nome1) + " e " + (nome2) + "! Vamos começar a jogar!\n")

  print("Escolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
  jogador1 = int(input("A escolha de " + (nome1) + " é: "))
  jogador2 = int(input("A escolha de " + (nome2) + " é: "))
  sair = 0 or 1
  pontos1 = 0
  pontos2 = 0

  while sair != 0:
    if jogador1 == jogador2:
      print("\nVocês empataram!")
    elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
      print("\n" + (nome2) + " ganhou!")
      pontos2 += 1
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
      print("\n" + (nome1) + " ganhou!")
      pontos1 += 1

    print("\nVocê quer continuar o jogo?")
    sair = int(input("Se você quiser continuar, aperte 1. Se quiser sair, aperte 0: "))

    if sair == 0:
      print("\nObrigado! \n\n---| Placar |---- \n" + (nome1) + " x " + (nome2) + "\n" + str(pontos1) + " x " + str(pontos2))
    else:
      print("\nEscolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
      jogador1 = int(input("A escolha de " + (nome1) + " é: "))
      jogador2 = int(input("A escolha de " + (nome2) + " é: "))


##modalidade 2 - humano x computador
elif modalidade == 2:
  nome = input("\nDigite o seu nome aqui: ")
  print("\nOlá, " + (nome) + "! Vamos começar jogar!\n")

  import random

  opcao = [1, 2, 3]
  jogador2 = random.choice(opcao)
  sair = 0 or 1
  pontos1 = 0
  pontos2 = 0
  print("Escolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
  jogador1 = int(input("A sua escolha é: "))

  while sair != 0:
    if jogador1 == jogador2:
      print("O computador jogou " + str(jogador2) + "\nVocês empataram!")
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
      print("O computador jogou " + str(jogador2) + "\n" + (nome) + " ganhou!")
      pontos1 += 1
    elif (jogador1 == 2 and jogador2 == 3) or (jogador1 == 1 and jogador2 == 2) or (jogador1 == 3 and jogador2 == 1):
      print("O computador jogou " + str(jogador2) + "\n" + "O computador ganhou!")
      pontos2 += 1

    print("\nVocê quer continuar o jogo?")
    sair = int(input("Se quiser continuar, aperte 1. Se quiser sair, aperte 0: "))
    
    if sair == 0:
      print("\nObrigado! \n\n---| Placar |---- \n" + (nome) + " x computador" + "\n" + str(pontos1) + " x " + str(pontos2))
    else:
      print("\nEscolha uma das três opções:\n1(Pedra) \n2(Papel) \n3(Tesoura)\n")
      jogador1 = int(input("A sua escolha é: "))
      jogador2 = random.choice(opcao)

##modalidade 3 - computador x computador
elif modalidade == 3:
  import random

  select = [1, 2, 3]
  jogador1 = random.choice(select)
  jogador2 = random.choice(select)
  sair = 0 or 1
  pontos1 = 0
  pontos2 = 0

  while sair != 0:
    if jogador1 == jogador2:
      print("O computador 1 jogou " + str(jogador1) + "\nO computador 2 jogou " + str(jogador2) + "\nEmpate!")
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
      print("O computador 1 jogou " + str(jogador1) + "\nO computador 2 jogou " + str(jogador2) + "\nO computador 1 ganhou!")
      pontos1 += 1
    elif (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 1):
      print("O computador 1 jogou " + str(jogador1) + "\nO computador 2 jogou " + str(jogador2) + "\nO computador 2 ganhou!")
      pontos2 += 1

    print("\nVocê quer continuar o jogo?")
    sair = int(input("Se quiser continuar, aperte 1. Se quiser sair, aperte 0:\n"))

    if sair == 0:
      print("\nObrigado! \n\n---| Placar |---- \n" + "computador 1 x computador 2" + "\n" + str(pontos1) + " x " + str(pontos2))
    else:
      print("Escolha um número entre desses três opções.\n 1(Pedra) 2(Papel) 3(Tesoura)\n")
      jogador1 = random.choice(select)
      jogador2 = random.choice(select)