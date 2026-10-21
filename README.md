Projeto 1 – Explorando PA e PG

Objetivo

Neste projeto, você deverá desenvolver um programa em Python capaz de gerar e analisar Progressões Aritméticas (PA) e Progressões Geométricas (PG).

O objetivo é relacionar os conceitos matem ́aticos estudados com elementos do

Pensamento Computacional, transformando padr ̃oes matematicos em algoritmos.

Etapa 1 – Planejamento
Antes de iniciar a programacão, tenta lembrar:
1. Quais informações são necessárias para construir uma PA?
2. Quais informações são necessárias para construir uma PG?
3. Como podemos determinar o próximo termo de uma PA?
4. Como podemos determinar o próximo termo de uma PG?
5. Como podemos calcular a soma dos termos gerados?
6. Elabore um pequeno pseudocódigo ou fluxograma representando o funcionamento do programa que você pretende construir.

Etapa 2 – Construindo o programa
Desenvolva um programa em Python que permita ao usuário escolher entre uma Progressão Aritmética e uma Progressão Geométrica.
Ao iniciar, o programa deverá apresentar um menu semelhante ao seguinte:
========================
PA & PG LAB
========================
1 - Progressão Aritmética

2 - Progressão Geométrica
Escolha:
Após a escolha, o programa deverá solicitar:
• o primeiro termo;
• a raz ̃ao;
• a quantidade de termos.
Exemplo 1 – Progressão Aritmética
Escolha: 1
Primeiro termo: 5
Razão: 3
Quantidade de termos: 6
O programa deverá apresentar:
PA gerada:
5, 8, 11, 14, 17, 20
Ultimo termo: 20
Soma dos termos: 75
Exemplo 2 – Progressão Geométrica
Escolha: 2
Primeiro termo: 2
Razão: 3
Quantidade de termos: 5
O programa deverá apresentar:
PG gerada:
2, 6, 18, 54, 162
Ultimo termo: 162
Soma dos termos: 242

Etapa 3 – Regra de implementação
A sequência deverá ser construída termo a termo, utilizando uma estrutura de repetição, como for ou while. Nesta etapa, não utilize apenas as fórmulas prontas do termo geral ou da soma dos termos para produzir os resultados.
O programa deverá gerar cada termo da sequência e, durante esse processo, calcular também a soma dos termos.

Etapa 4 – Testando o programa
Depois de finalizar o programa, realize pelo menos quatro testes:
1. uma PA crescente;
2. uma PA decrescente;
3. uma PG crescente;
4. uma PG decrescente.
Para cada caso, registre os valores utilizados e o resultado obtido. Em seguida, faça uma verificação matemática para confirmar se a sequência e a soma calculadas pelo programa estão corretas.

Etapa 5 – Reflexão
Após concluir o programa, responda:
1. Qual foi a principal diferença entre o algoritmo utilizado para gerar uma PA e o utilizado para gerar uma PG?
2. Qual foi a função da estrutura de repetição no seu programa?
3. Qual foi a maior dificuldade encontrada durante a programação?
4. Como você resolveu essa dificuldade?

Etapa 6 – Alcançando a Meta
Modifique o programa para resolver o seguinte problema:

Dado o primeiro termo, a raz ̃ao e um valor definido como meta, determine quantos termos são necessários para que a soma dos termos da progressão ultrapasse essa meta.
Por exemplo:

Tipo: PG
Primeiro termo: 2
Razao: 2
Meta: 1000
Resultado:
Sao necessarios 9 termos.
Soma obtida: 1022
Neste desafio, o número de termos não ser ́a informado pelo usuário. O próprio programa dever ́a descobrir quando a soma ultrapassar ́a a meta.

Etapa 7 – Frontend

Os estudantes interessados poderão desenvolver uma interface gráfica (frontend) para o programa. A interface dever ́a permitir ao usu ́ario:

• escolher entre PA e PG;
• informar o primeiro termo;
• informar a raz ̃ao;
• informar a quantidade de termos;
• visualizar a sequˆencia gerada;
• visualizar o  ́ultimo termo;
• visualizar a soma dos termos.
Poderá ser utilizada qualquer tecnologia para construção da interface, como Tkinter, Streamlit, HTML/CSS/JavaScript ou outra solução escolhida pelo estudante.
Entregáveis
Deverão ser entregues:
1. o código-fonte do programa em Python (.py);
2. o pseudocódigo ou fluxograma elaborado na Etapa 1;
3. os quatro testes realizados na Etapa 4;
4. as respostas às questões da Etapa 5;
5. o frontend, caso o estudante opte pelo desafio extra.

Critérios de Avaliação
Critério de Pontuação
Funcionamento correto do programa 1,5
Geração correta de PA e PG 1,0
Cálculo correto da soma 1,0
Uso adequado de estruturas de repetição e decisão 1,0
Organização e clareza do código 0,5
Realização e verificação dos testes 0,5
Respostas e reflexção sobre o desenvolvimento 0,5
Resolução do problema “Quando a Soma Atinge a Meta?” 1,0
Desenvolvimento do frontend 3,0
Total 10,0
