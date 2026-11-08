def prompt():
  while True:
    escolha = input(" 1. soma\n 2. subtrair\n 3. multiplicar\n 4. dividir\n Digite sua escolha: ")
    if escolha.isdigit() and 1 <= int(escolha) <= 4: #comando para conferir se é um numero
      break #sai do laço se a escolha for válida
    print("Operações disponiveis apenas de 1 à 4, escolha novamente: ")
  x = int(input("Digite o primeiro numero..."))
  y = int(input("Digite o segundo numero..."))
  return int(escolha), x, y

def som(x, y):
  soma = x + y
  return soma

def mult(x, y):
  multi = x * y
  return multi

def sub(x, y):
  subtr = x - y
  return subtr

def div(x, y):
  if y == 0:
    return "Não é possível fazer divisão por zero"
  divis = x / y
  return divis    

def calculadora():
  escolha, x, y = prompt() # chama a função do prompt e distriu os valores da função
  if escolha == 1:
    resultado = som(x, y)
  elif escolha == 2:  
    resultado = sub(x, y)
  elif escolha == 3:
    resultado = mult(x, y)
  elif escolha == 4:
    resultado = div(x, y)
  print("Resultado: ", resultado)
  continuar = input("\nDeseja continuar? (S/N): ").strip().upper()
  if continuar == "S":
    calculadora() #Recursividade, chamando a si mesmo para reiniciar o processo
  else:
    print("Programa Encerrado!")

calculadora() #chama todo o programa inicialmente