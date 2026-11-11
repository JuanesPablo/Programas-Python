lista_afazer = [] #lista vazia 
def mostrar_lista():                   #for index, tarefa in enumerate(lista_afazer, start=1):
  index = 1                            #  print(f"{index}. {tarefa}")                            
  for tarefa in lista_afazer:          #forma alternativa de fazer uma contagem
    print(f"{index}. {tarefa}")
    index += 1 #incremento de +1

print("Bem-vindo à sua lista de Afazeres!")
while True:
  while True: #looping para que acerte a opção
    escolha = input("\nEscolha uma opção:\n1) Adicione uma Tarefa\n2) Remover última Tarefa\n3) Mostrar Lista\n4) Mover/Reordenar Tarefa\n5) Encerrar Programa\nEntre com sua escolha: ")
    if escolha.isdigit() and escolha in ["1", "2", "3", "4", "5"]: #comando que procura se escolha está dentro do array e se é número
      break
    print("\nEscolha uma opção disponível e que seja um número!")  
  if escolha == "1":
    while True:
      nova_tarefa = input("\nAdicione uma Tarefa: ").capitalize() #comando que faz a primeira letra ficar maiuscola
      lista_afazer.append(nova_tarefa)
      print() #apenas para pular uma linha
      mostrar_lista()
      while True: #looping para que acerte o (S/N)
        continuar = input("\nAdicionar mais uma Tarefa? (S/N): ").lower() #deixa qualquer entrada minuscula
        if continuar in ["s", "n"]:
          break
        print("Escolha entre (S/N)")
      if continuar == "n": #apenas o "n" vai fazer sair do looping de add tarefas
        break  
  elif escolha == "2":
    if len(lista_afazer) == 0:
      print("\nSua lista de Afazeres está vazia!")
    else:
      lista_afazer.pop()
      if len(lista_afazer) == 0: #avisa assim que o último item foi removido
        print("\nVocê removeu o último item. A lista agora está vazia!")
      else:  
        print()
        mostrar_lista()
  elif escolha == "3":
    if len(lista_afazer) == 0:
      print("\nSua lista está vazia!")
    else:
      print()
      mostrar_lista()
  elif escolha == "4":
    if len(lista_afazer) < 2:
      print("\nA lista precisa ter pelo menos duas tarefas para poder reordena-la.")
    else:
      while True:
        print("\nLista Atual:")
        mostrar_lista()
        entrada_antiga = input("Qual o número da Tarefa que gostaria de mudar: ") 
        entrada_nova = input("Qual a posição (número) que gostaria que a Tarefa ficasse: ")
        if entrada_antiga.isdigit() and entrada_nova.isdigit(): #verifica se são numeros
          posicao_antiga = int(entrada_antiga) -1 #-1 para ficar dentro so indice do array, validando a proxima regra do if
          posicao_nova = int(entrada_nova) -1
          if 0 <= posicao_antiga < len(lista_afazer) and 0 <= posicao_nova < len(lista_afazer):
            tarefa_movida = lista_afazer.pop(posicao_antiga) #peguei a informação removida
            lista_afazer.insert(posicao_nova, tarefa_movida) #muda de posição na lista
            print("\nTarefas reorganizadas com Sucesso!")
            print("\nLista Atual:")
            mostrar_lista()
            break
          else:
            print("\nPosição inválida! Tente Novamente.")
        else:
          print("Digite apenas números, por favor!")    
  elif escolha == "5":
    print("\nEncerrando Programa..")
    break


#Lembrete de listas:
#lista = [1,2,3,4,5,6]
#lista.append(7) #adiciona sempre no final da lista
#lista.insert(2, "aqui") #adiciona um valor na posiçao do indice que quer
#lista.pop(2) #remove um valor do indice que colocou ou () para ser do ultimo
#new = lista.pop() #retorna o valor removido 
#lista.remove(2) #apaga o valor do indice e retorna nulo, assim como del lista[2]
#print(len(lista)) #informa o numero de elementos na lista
#max(lista) #mostra o maior valor da lista
#min(lista) #mostra o menor vslor da lista
#lista.sort() #ordena a lista de numeros em ordem crescente e de strg em ordem alfabetica
#sum(lista) #soma todos os valores numericos da lista 
#print(lista.count(2)) #mostra quantas vezes esse elemento aparece na lista
#print(2 in lista) #retorna True ou False se tiver esse valor na lista 
#print(lista)