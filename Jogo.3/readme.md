# 🧮 Calculadora Simples em Python

Um aplicativo de calculadora interativo desenvolvido para rodar diretamente no terminal. Este projeto faz parte dos meus estudos práticos de lógica de programação em Python, focando em estruturação de código com funções (`def`), controle de fluxo com loops (`while`), tratamento de recursividade, validações de entrada e operações matemáticas básicas.

---

## 🚀 Funcionalidades

* **Operações Básicas:** Realiza cálculos de Adição, Subtração, Multiplicação e Divisão entre dois números informados pelo usuário.
* **Validação de Escolha de Operação:** Utiliza validação numérica rigorosa com o método `.isdigit()` combinado com checagem de intervalo (`1 <= int(escolha) <= 4`) para garantir que o usuário selecione apenas opções válidas no menu.
* **Proteção contra Divisão por Zero:** Conta com uma verificação inteligente na função de divisão que impede quebras no sistema caso o divisor seja `0`, retornando uma mensagem informativa.
* **Modularização por Funções:** O código é totalmente dividido em responsabilidades específicas (`prompt()`, `faz_soma()`, `faz_subtracao()`, `faz_multiplicacao()`, `faz_divisao()` e `calculadora()`), facilitando a manutenção e a legibilidade.
* **Reinicialização por Recursividade:** Permite reiniciar o programa de forma fluida utilizando chamadas recursivas controladas (`calculadora()`), ou encerrá-lo de maneira limpa através de confirmação (`S/N`).
* **Limpeza e Normalização de Textos (`.strip()` e `.lower()`):** 
  * O método `.strip()` é aplicado nas entradas de confirmação para remover automaticamente qualquer espaço em branco acidental que o usuário possa digitar antes ou depois da letra (por exemplo, transformando `" s "` em `"s"`).
  * O método `.lower()` converte instantaneamente o texto digitado em letras minúsculas. Combinado com o `.strip()`, ele garante que o programa reconheça a resposta do usuário perfeitamente, independentemente de ele digitar `"S"`, `"s"`, `"SIM"` ou com espaços extras ao redor.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**

---

## 📥 Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina. Siga os passos abaixo:

1. Clone este repositório ou faça o download do arquivo `calculadoraSimples.py`:
   ```bash
   git clone https://github.com/JuanesPablo/Programas-Python.git

2. Navegue até a pasta do projeto pelo terminal:
   ```bash
   cd Programas-Python

3. Execute o script Python (substitua pelo nome exato do seu arquivo, por exemplo):
    ```bash
   python calculadoraSimples.py