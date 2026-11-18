# 🃏 Simulador de Baralho Interativo em Python

Um aplicativo de simulação de baralho de cartas desenvolvido para rodar diretamente no terminal. Este projeto faz parte dos meus estudos práticos de lógica de programação em Python, avançando para conceitos mais robustos como estruturação de dados complexos (tuplas e listas), manipulação de módulos nativos (`random`, `os`, `time`), funções customizadas com tratamento de múltiplos fluxos de exibição e formatação de texto em blocos gráficos via terminal.

---

## 🚀 Funcionalidades

* **Múltiplos Modos de Jogo Interativos:**
  * **[1] Mesa Acumulada:** Todas as cartas puxadas ao longo das rodadas ficam acumuladas e reveladas na mesa em blocos organizados, permitindo visualizar o histórico completo da partida.
  * **[2] Mão por Rodada:** Foca na jogada atual, exibindo lado a lado apenas as cartas puxadas no último comando do usuário em blocos de até 7 colunas.
  * **[3] Carta por Carta:** Utiliza uma função de renderização unitária para desenhar e exibir individualmente cada carta gerada na última rodada.
* **Geração e Embaralhamento Automático (`criar_deck`):** Cria um baralho padrão de 52 cartas combinando naipes e valores, embaralhando-os de forma totalmente aleatória a cada nova partida.
* **Validação de Entrada Robusta:** O sistema trata entradas incorretas (letras em vez de números, valores negativos ou vazios) usando verificações como `.isdigit()`, solicitando novas tentativas sem quebrar a execução.
* **Comando de Saída Flexível:** Permite que o usuário retorne ao menu principal a qualquer momento digitando `'sair'` durante as rodadas.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto faz uso intensivo de bibliotecas nativas da linguagem Python para garantir performance, controle de fluxo e interação visual:

* **Python 3.x:** Linguagem base utilizada para estruturar todo o código, tipagem e lógica de execução.
* **Módulo `random`:** Utilizado especificamente através da função `random.shuffle()` para embaralhar aleatoriamente a ordem das cartas no baralho recém-criado, garantindo imprevisibilidade a cada rodada.
* **Módulo `os`:** Empregado na função `limpar_tela()`, utilizando `os.system('cls' if os.name == 'nt' else 'clear')` para limpar o terminal dependendo do sistema operacional (Windows ou sistemas Unix/Linux/macOS), proporcionando uma interface limpa e fluida.
* **Módulo `time`:** Utilizado para criar pausas estratégicas na execução do programa (como o `time.sleep(2)` na tela de boas-vindas), melhorando a experiência de transição visual para o usuário.

---

## 💡 Conceitos Praticados e Guia Técnico

Durante o desenvolvimento deste projeto, aprofundei o uso de estruturas de dados fundamentais do Python, combinando coleções mutáveis e imutáveis para otimizar a lógica do baralho:

### 1. Representação Visual com Arte ASCII
Como o terminal de texto tradicional não exibe imagens gráficas nativas, o projeto utiliza **Arte ASCII** para desenhar as cartas utilizando caracteres de texto (`+`, `-`, `|` e espaços):
* **Alinhamento com `.ljust(2)` e `.rjust(2)`:** Como diferentes cartas possuem larguras de texto variadas (por exemplo, o número `"10"` ocupa dois caracteres enquanto o `"A"` ocupa um), esses métodos garantem que os valores fiquem perfeitamente centralizados e alinhados dentro da moldura, impedindo que o layout gráfico quebre.

### 2. A Matemática dos `for` Alinhados e Tuplas (`criar_deck`)
A função de criação do baralho é um exemplo clássico da união entre loops aninhados e estruturas de dados imutáveis:
* **Tuplas (`tuple`):** Cada carta é representada por uma tupla imutável `(naipe, rank)`, como `("♥", "A")`. O uso de tuplas garante a integridade dos dados da carta, impedindo que seus atributos sejam alterados acidentalmente durante o jogo e consumindo menos memória.
* **Loops `for` Aninhados:** O primeiro loop `for naipe in naipes:` percorre os naipes (`naipes = ["♥", "♦", "♣", "♠"]`), enquanto o loop interno `for rank in ranks:` percorre todos os valores de `ranks` do início ao fim para cada naipe. Para cada iteração combinada, o script executa `deck.append((naipe, rank))`, empacota o par em uma tupla e adiciona à lista, gerando automaticamente as **52 cartas** do baralho.

### 3. Exibição Lado a Lado (`mostrar_lado_a_lado`)
Para exibir as cartas lado a lado em vez de empilhadas, o código utiliza fatiamento de listas (*slicing*) e loops de montagem linha a linha:
* **Fatiamento por Blocos:** Com `for i in range(0, len(mao), 7):` e `bloco = mao[i:i+7]`, o código divide a mão em blocos de até 7 cartas por linha, evitando que o terminal fique horizontalmente poluído.
* **Construção Linha a Linha:** Usando `for j in range(7):` junto com `linhas[j] += cartas_alinhada[j] + "  "`, o programa percorre as 7 linhas verticais da carta ASCII e vai "costurando" as cartas vizinhas lado a lado na mesma linha do terminal.

### 4. Controle de Fluxo com `while`
* O **`while True`** atua como o motor principal do menu interativo e das rodadas, garantindo que o programa continue rodando de forma fluida até que o usuário decida sair explicitamente.
* Também é aplicado na validação de dados de entrada, travando o fluxo caso o usuário digite caracteres inválidos e forçando o reenvio correto da resposta.

---

## 📥 Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina. Siga os passos abaixo:

1. Clone este repositório ou faça o download do arquivo `baralhoDeCartas.py`:
   ```bash
   git clone https://github.com/JuanesPablo/Programas-Python.git

2. Navegue até a pasta do projeto pelo terminal:
   ```bash
   cd Programas-Python

3. Execute o script Python (substitua pelo nome exato do seu arquivo, por exemplo):
    ```bash
   python baralhoDeCartas.py