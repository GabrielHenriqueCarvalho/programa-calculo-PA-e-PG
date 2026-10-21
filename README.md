# Projeto 1 – Explorando PA e PG

## Objetivo
Neste projeto, você deverá desenvolver um programa em Python capaz de gerar e analisar Progressões Aritméticas (PA) e Progressões Geométricas (PG).
O objetivo é relacionar os conceitos matemáticos estudados com elementos do Pensamento Computacional, transformando padrões matemáticos em algoritmos.

---

## Etapa 1 – Planejamento
Antes de iniciar a programação, tenta lembrar:
1. Quais informações são necessárias para construir uma PA?
2. Quais informações são necessárias para construir uma PG?
3. Como podemos determinar o próximo termo de uma PA?
4. Como podemos determinar o próximo termo de uma PG?
5. Como podemos calcular a soma dos termos gerados?
6. Elabore um pequeno pseudocódigo ou fluxograma representando o funcionamento do programa que você pretende construir.

---

## Etapa 2 – Construindo o programa
Desenvolva um programa em Python que permita ao usuário escolher entre uma Progressão Aritmética e uma Progressão Geométrica.

Ao iniciar, o programa deverá apresentar um menu semelhante ao seguinte:
```text
========================
PA & PG LAB
========================
1 - Progressão Aritmética

2 - Progressão Geométrica
Escolha:
```

Após a escolha, o programa deverá solicitar:
* O primeiro termo;
* A razão;
* A quantidade de termos.

### Exemplo 1 – Progressão Aritmética
* **Escolha:** 1
* **Primeiro termo:** 5
* **Razão:** 3
* **Quantidade de termos:** 6

O programa deverá apresentar:
```text
PA gerada:
5, 8, 11, 14, 17, 20
Ultimo termo: 20
Soma dos termos: 75
```

### Exemplo 2 – Progressão Geométrica
* **Escolha:** 2
* **Primeiro termo:** 2
* **Razão:** 3
* **Quantidade de termos:** 5

O programa deverá apresentar:
```text
PG gerada:
2, 6, 18, 54, 162
Ultimo termo: 162
Soma dos termos: 242
```

---

## Etapa 3 – Regra de implementação
A sequência deverá ser construída termo a termo, utilizando uma estrutura de repetição, como `for` ou `while`. Nesta etapa, não utilize apenas as fórmulas prontas do termo geral ou da soma dos termos para produzir os resultados.

O programa deverá gerar cada termo da sequência e, durante esse processo, calcular também a soma dos termos.

---

## Etapa 4 – Testando o programa
Depois de finalizar o programa, realize pelo menos quatro testes:
1. Uma PA crescente;
2. Uma PA decrescente;
3. Uma PG crescente;
4. Uma PG decrescente.

Para cada caso, registre os valores utilizados e o resultado obtido. Em seguida, faça uma verificação matemática para confirmar se a sequência e a soma calculadas pelo programa estão corretas.

---

## Etapa 5 – Reflexão
Após concluir o programa, responda:
1. Qual foi a principal diferença entre o algoritmo utilizado para gerar uma PA e o utilizado para gerar uma PG?
2. Qual foi a função da estrutura de repetição no seu programa?
3. Qual foi a maior dificuldade encontrada durante a programação?
4. Como você resolveu essa dificuldade?

---

## Etapa 6 – Alcançando a Meta
Modifique o programa para resolver o seguinte problema:

Dado o primeiro termo, a razão e um valor definido como meta, determine quantos termos são necessários para que a soma dos termos da progressão ultrapasse essa meta.

Por exemplo:
* **Tipo:** PG
* **Primeiro termo:** 2
* **Razao:** 2
* **Meta:** 1000

Resultado:
```text
Sao necessarios 9 termos.
Soma obtida: 1022
```

Neste desafio, o número de termos não será informado pelo usuário. O próprio programa deverá descobrir quando a soma ultrapassará a meta.

---

## Etapa 7 – Frontend
Os estudantes interessados poderão desenvolver uma interface gráfica (frontend) para o programa. A interface deverá permitir ao usuário:
* Escolher entre PA e PG;
* Informar o primeiro termo;
* Informar a razão;
* Informar a quantidade de termos;
* Visualizar a sequência gerada;
* Visualizar o último termo;
* Visualizar a soma dos termos.

Poderá ser utilizada qualquer tecnologia para construção da interface, como Tkinter, Streamlit, HTML/CSS/JavaScript ou outra solução escolhida pelo estudante.

---

## Entregáveis
Deverão ser entregues:
1. O código-fonte do programa em Python (.py);
2. O pseudocódigo ou fluxograma elaborado na Etapa 1;
3. Os quatro testes realizados na Etapa 4;
4. As respostas às questões da Etapa 5;
5. O frontend, caso o estudante opte pelo desafio extra.

---

## Critérios de Avaliação

| Critério | Pontuação |
| :--- | :--- |
| Funcionamento correto do programa | 1,5 |
| Geração correta de PA e PG | 1,0 |
| Cálculo correto da soma | 1,0 |
| Uso adequado de estruturas de repetição e decisão | 1,0 |
| Organização e clareza do código | 0,5 |
| Realização e verificação dos testes | 0,5 |
| Respostas e reflexão sobre o desenvolvimento | 0,5 |
| Resolução do problema “Quando a Soma Atinge a Meta?” | 1,0 |
| Desenvolvimento do frontend | 3,0 |
| **Total** | **10,0** |
