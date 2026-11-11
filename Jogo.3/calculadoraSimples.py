print("Bem-vindos, a nossa calculadora simples.\n")

def prompt():
  while True:
    escolha = input(" 1. soma\n 2. subtrair\n 3. multiplicar\n 4. dividir\n Digite sua escolha: ")
    if escolha.isdigit() and 1 <= int(escolha) <= 4: #comando para conferir se é um numero
      break #sai do laço se a escolha for válida
    print("Operações disponiveis apenas de 1 à 4, escolha novamente: ")
  x = int(input("\nDigite o primeiro numero: "))
  y = int(input("Digite o segundo numero: "))
  return int(escolha), x, y

def faz_soma(x, y):
  return x + y

def faz_multiplicacao(x, y):
  return x * y

def faz_subtracao(x, y):
  return x - y

def faz_divisao(x, y):
  if y == 0:
    return "Não é possível fazer divisão por zero"
  return x / y   

def calculadora():
    escolha, x, y = prompt() # chama a função do prompt e distriu os valores da função
    if escolha == 1:
      resultado = faz_soma(x, y)
    elif escolha == 2:  
      resultado = faz_subtracao(x, y)
    elif escolha == 3:
      resultado = faz_multiplicacao(x, y)
    elif escolha == 4:
      resultado = faz_divisao(x, y)
    print("Resultado: ", resultado)
    while True:
      continuar = input("\nDeseja continuar? (S/N): ").strip().lower() #strip corta espaços vazios antes ou depois
      if continuar == "s":
        calculadora() #Recursividade, chamando a si mesmo para reiniciar o processo
        break
      elif continuar == "n":
        print("Programa Encerrado!")
        break #precisa de 2 break para encerrar de vez a recursividade
      else:
        print("Selecione apenas (S/N), por favor!")

calculadora() #chama todo o programa inicialmente