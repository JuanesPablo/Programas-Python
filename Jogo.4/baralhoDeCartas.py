import random #permite trabalhar com valores aletórios
import os #interage com alg func do sist
import time #trabalha com tempo e pausas na execução

def limpar_tela(): #função para limpar a tela em Windowns usando a biblioteca
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_deck():
    naipes = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for naipe in naipes: #for aninhado para criar tuplas
        for rank in ranks:
            deck.append((naipe, rank))
    random.shuffle(deck) #usa a biblioteca para misturar lista de tuplas
    return deck

def compra_carta(deck, quantidade): #compra uma carta por vez
    mao = []
    for i in range(quantidade):
        if deck: #verifica se tem elementos
            mao.append(deck.pop()) #adiciona na mão a carta retirada
        else:
            break
    return mao, deck

def mostrar_cartas(carta): # Função para mostrar uma carta individual
    naipe, rank = carta
    r1 = rank.ljust(2) # compl o texto com esp a diretia
    r2 = rank.rjust(2) #completa com esp a esquerda
    print(f"""+-------+
| {r1}    |
|       |
|   {naipe}   |
|       |
|    {r2} |
+-------+""")

def mostrar_lado_a_lado(mao): # Função para mostrar cartas lado a lado em blocos de 7 (usada nos Modos 1 e 2)
    for i in range(0, len(mao), 7): #for com parametros, começa no 0 - termina de acordo com o tam da mão - avança no intervalo de 7(separa em blocos de 7)
        bloco = mao[i:i+7] #fatiamento de lista(slicing), seleciona 7 cartas a partir do i
        linhas = ["", "", "", "", "", "", ""] #a ideia seria juntar a primeira linha de todas as cartas da fileira e assim por diante, das 7 linhas que montam a carta
        for carta in bloco: #percorre todas as cartas daquele bloco
            naipe, rank = carta
            r1 = rank.ljust(2) 
            r2 = rank.rjust(2)
            cartas_alinhada = ["+-------+",
                              f"| {r1}    |",
                               "|       |",
                              f"|   {naipe}   |",
                               "|       |",
                              f"|    {r2} |",
                               "+-------+"]
            for j in range(7): #coloca as cartas lado a lado, percorrendo as 7 linhas
                linhas[j] += cartas_alinhada[j] + "  "       
        for linha in linhas: #percorre as 7 linhas já montadas e as imprime
            print(linha)
        print()

def iniciar_jogo():
    limpar_tela() #limpa o que tem antes
    print("=========================================\n       BEM-VINDO AO JOGO DE CARTAS       \n=========================================\n")
    time.sleep(2) #deixa a mensagem mostrando por 2s 
    while True:
        limpar_tela()
        print("MENU PRINCIPAL:\n [1] Mesa Acumulada (todas as cartas puxadas ficam reveladas)\n [2] Mão por Rodada (mostra as cartas lado a lado a cada pedido)\n" \
        " [3] Carta por Carta (mostra usando a função unitária)\n [4] Encerrar programa")        
        modo = input("\nEscolha uma opção (1 a 4): ")
        if modo == "4":
            print("\nSaindo do programa... Gudi Bai! 👋")
            break
        while modo not in ["1", "2", "3"]:
            print("⚠️ Opção inválida! Digite um número de 1 a 4.")
            modo = input("Escolha uma opção (1 a 4): ")
            if modo == "4":
                print("\nSaindo do programa... Gudi Bai! 👋")
                return
        #iniciando as variaveis e o deck
        deck = criar_deck()
        mao_acumulada = [] #modo 1         
        ultima_mao = []    #modo 2        
        ultimas_cartas_modo3 = [] #modo 3 
        primeira_rodada = True

        while len(deck) > 0:
            if modo == "1" or primeira_rodada: #verifica se o programa já passou da primeira rodada(em todos os jogos) e garante a limpe subsequente
                limpar_tela()
                primeira_rodada = False
            if modo == "1" and len(mao_acumulada) > 0:
                print(f"Suas cartas acumuladas na mesa ({len(mao_acumulada)} reveladas):\n")
                mostrar_lado_a_lado(mao_acumulada)
                print("=" * 50)  
            elif modo == "2" and len(ultima_mao) > 0:
                limpar_tela()
                print(f"Última mão puxada ({len(ultima_mao)} cartas):\n")
                mostrar_lado_a_lado(ultima_mao)
                print("=" * 50)   
            elif modo == "3" and len(ultimas_cartas_modo3) > 0:
                limpar_tela()
                print(f"Últimas cartas puxadas (Modo Carta por Carta):\n")
                for carta in ultimas_cartas_modo3: #percorre cada carta e mostra uma por uma
                    mostrar_cartas(carta)
                    print()
                print("=" * 50)
            print(f"\nCartas restantes no baralho: {len(deck)}")
            entrada = input("Quantas cartas você deseja puxar? (ou digite 'sair' para voltar ao menu): ") #Entrada importante para iniciar a MAO
            if entrada.lower() == "sair": #valida a saida do jogo atual
                print("\nVoltando ao menu principal...")
                break
            if entrada.isdigit():
                quantidade = int(entrada)
                if quantidade <= 0:
                    print("Por favor, escolha um número maior que zero.")
                    continue # interrompe a exec atual e volta ao inicio do loop(ou o prox)
            else:
                print("⚠️ Entrada inválida! Digite apenas números inteiros.") 
                continue 
            novas_cartas, deck = compra_carta(deck, quantidade) #chama a função de compra cartas e atualiza o deck
            if modo == "1": #.extend adiciona a como parte da lista atual(melhor que .append)
                mao_acumulada.extend(novas_cartas)
            elif modo == "2": #substitui a mão do jogador para funcionar nas funções
                ultima_mao = novas_cartas
            elif modo == "3":
                ultimas_cartas_modo3 = novas_cartas

        if len(deck) == 0: #apresenta o final do deck
            limpar_tela()
            print("--- FIM DO JOGO: O baralho acabou! ---\n")
            if modo == "1":
                print(f"Sua mesa final acumulada com {len(mao_acumulada)} cartas:\n")
                mostrar_lado_a_lado(mao_acumulada) #mostra todas acumuladas na partida
            print("=" * 50)
            escolha_fim = input("\nDeseja voltar ao menu inicial? (1 para menu, 2 para encerrar): ")
            if escolha_fim == "2":
                print("\nObrigado por jogar! Até a próxima. 👋")
                break

iniciar_jogo()