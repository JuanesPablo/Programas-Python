# 📝 Gerenciador de Tarefas (To-Do List) em Python

Um aplicativo interativo de lista de afazeres desenvolvido para rodar diretamente no terminal. Este projeto faz parte dos meus estudos práticos de lógica de programação em Python, focando em manipulação de estruturas de dados (listas), controle de fluxo avançado, tratamento de entradas do usuário e modularização de código com funções.

---

## 🚀 Funcionalidades

* **Adicionar Tarefas:** Insira novas tarefas na sua lista utilizando o método `.append()` para adicioná-las sempre ao final da estrutura, combinado com formatação inteligente via `.capitalize()` para garantir que a primeira letra de cada tarefa fique sempre maiúscula.
* **Remover o Último Item:** Remova a última tarefa adicionada usando o método `.pop()`, com avisos dinâmicos caso a lista fique vazia.
* **Exibir Lista:** Visualize todas as tarefas cadastradas de forma numerada e organizada, com a modularização de funções `def mostrar_lista()`, para evitar repetições desnecessárias de blocos de código.
* **Mover / Reordenar Tarefas:** Reorganize a posição de qualquer tarefa informando o número atual e para onde ela deve ir, combinando `.pop(indice)` e `.insert(indice, valor)`.
* **Validação Robusta:** O programa trata entradas incorretas (letras em vez de números, opções inválidas ou posições inexistentes) usando verificações como `.isdigit()`, solicitando novas tentativas sem quebrar a execução.
* **Normalização de Textos (`Case-Insensitive`):** Utiliza métodos como `.lower()` em validações de continuidade (como o prompt de `S/N`) para aceitar variações de digitação do usuário.
* **Encerramento Controlado:** Encerre o programa de forma limpa a qualquer momento pela opção dedicada do menu.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**

---

## 💡 Conceitos Praticados e Guia de Métodos de Lista

Durante o desenvolvimento deste projeto, documentei e pratiquei alguns conceitos fundamentais da linguagem. Abaixo está o resumo técnico e o meu guia de anotações sobre manipulação de listas:

* `lista.append(item)` — Adiciona um elemento sempre no final da lista.
* `lista.insert(indice, valor)` — Adiciona um valor na posição do índice que você escolher.
* `lista.pop()` — Remove o último valor da lista.
* `lista.pop(indice)` — Remove um valor do índice que você colocou (e você pode salvar o valor removido em uma variável, ex: `new = lista.pop()`).
* `lista.remove(valor)` — Apaga o valor do índice e retorna nulo (assim como `del lista[2]`).
* `len(lista)` — Informa o número de elementos na lista.
* `max(lista)` — Mostra o maior valor da lista.
* `min(lista)` — Mostra o menor valor da lista.
* `lista.index(elemento)` — Retorna o índice (posição) da primeira ocorrência do elemento na lista.
* `lista.clear()` — Remove todos os elementos da lista, deixando-a vazia.
* `lista.sort()` — Ordena os números em ordem crescente e strings em ordem alfabética.
* `lista.reverse()` — Inverte a ordem dos elementos da lista de trás para frente.
* `sum(lista)` — Soma todos os valores numéricos da lista.
* `lista.count(elemento)` — Mostra quantas vezes esse elemento aparece na lista.
* `elemento in lista` — Retorna `True` ou `False` se tiver esse valor na lista.

---

## 📥 Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina. Siga os passos abaixo:

1. Clone este repositório ou faça o download do arquivo `listaDeAfazres.py`:
   ```bash
   git clone https://github.com/JuanesPablo/Programas-Python.git

2. Navegue até a pasta do projeto pelo terminal:
   ```bash
   cd Programas-Python

3. Execute o script Python (substitua pelo nome exato do seu arquivo, por exemplo):
    ```bash
   python listaDeAfazeres.py