import random #trás a biblioteca da escolha por acaso

player_wins = 0
computer_wins = 0 
choices = ["pedra","papel","tesoura"]

print("Vamos jogar Pedra, Papel ou Tesoura!")

while player_wins < 2 and computer_wins < 2:
  while True: 
    player_choice = input("\nAtençao jogador!\nEscolha entre Pedra, Papel ou Tesoura.\n").lower() #para qualquer que seja a entrada, fique minuscula
    if player_choice not in choices:
      print("Escolha a opção correta!")
  computer_choice = random.choice(choices) #aplicação da escolha por acaso
  print(f"Escolha do Computador: {computer_choice}")
  if (player_choice == "pedra" and computer_choice == "tesoura") or (player_choice == "papel" and computer_choice == "pedra") or (player_choice == "tesoura" and computer_choice == "papel"):
    winner ="Player"
    player_wins += 1
    print("\nVocê ganhou essa partida!")
  elif (player_choice == "pedra" and computer_choice == "pedra") or (player_choice == "papel" and computer_choice == "papel") or (player_choice == "tesoura" and computer_choice == "tesoura"):
    winner = "Empate"
    print("\nDeu empate!")
  else:
    winner = "Computer"
    computer_wins += 1
    print("\nComputador ganhou essa partida, pare de vacilar!")
  print(f"Placar atual: Jogador: {player_wins} - Computador: {computer_wins}")

if player_wins > computer_wins:
  print("\nParabéns! Você ganhou!")
else:
  print("\nComputador ganhou.. vacilou ein!")