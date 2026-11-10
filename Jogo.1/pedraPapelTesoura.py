import random #trás a biblioteca da escolha por acaso

jogador_vitorias = 0
computador_vitorias = 0 
escolhas = ["pedra", "papel", "tesoura"]

print("Vamos jogar Pedra, Papel ou Tesoura!")

while jogador_vitorias < 2 and computador_vitorias < 2:
  while True: #loop continua até acertar a palavra
    jogador_escolha = input("\nAtençao jogador!\nEscolha entre Pedra, Papel ou Tesoura.\n").strip().lower() #para qualquer que seja a entrada, fique minuscula
    if jogador_escolha in escolhas: #se escolher correto, pare senão
      break
    print("Escolha a opção correta!")
  computador_escolha = random.choice(escolhas) #aplicação da escolha por acaso
  print(f"Escolha do Computador: {computador_escolha}")
  if (jogador_escolha == "pedra" and computador_escolha == "tesoura") or (jogador_escolha == "papel" and computador_escolha == "pedra") or (jogador_escolha == "tesoura" and computador_escolha == "papel"):
    jogador_vitorias += 1
    print("\nVocê ganhou essa partida!")
  elif (jogador_escolha == "pedra" and computador_escolha == "pedra") or (jogador_escolha == "papel" and computador_escolha == "papel") or (jogador_escolha == "tesoura" and computador_escolha == "tesoura"):
    print("\nDeu empate!")
  else:
    computador_vitorias += 1
    print("\nComputador ganhou essa partida, pare de vacilar!")
  print(f"Placar atual: Jogador: {jogador_vitorias} - Computador: {computador_vitorias}")

if jogador_vitorias > computador_vitorias:
  print("\nParabéns! Você ganhou!")
else:
  print("\nComputador ganhou.. vacilou ein!")