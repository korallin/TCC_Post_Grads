# TCC da especialização do IMD/JFRN
**Trabalho do final do curso na JFRN**

Esse é o repositório do TCC da pós-graduação do IMD/JFRN, o objetivo é, basicamente, criar um painel que seja fácil de ler, minimalista e fácil de ser distribuído, e precisa mostrar informações sobre as distrubições dos processos pelas Varas do Rio Grande do Norte, por enquanto podemos nos concentrar em poucas Varas e escalar com o tempo. 

Algumas ferramentas usadas aqui serão o PostgreSQL (e o pgAdmin) que é o banco de dados usado na Justiça Federal do RN, e também alguma ferramenta de geração de painel, muito provável que seja em Python, as candidatas são: dash, pyxley e bokeh. 

Os campos mostrados serão: 

- número do processo
- data do ajuizamento
- dados das partes (identificação e advogados)
- dados dos assuntos cadastrados
- classe processual
- vara 
- todas as movimentações processuais

Objetivo da entrega: 

- Rotina de extração dos dados usando o PostgreSQL
- Servidor HTTP rodando o painel
- Estudar cronjobs

To Do:

- <s>Estudar os códigos das estudantes de Iniciação Científica do Professor Elias</s>
- <s>Terminar o curso de PostgreSQL da Udemy</s>
- Pesquisar materiais de criação de Dashboards usando Python - trabalho constante
- Melhorar o visual do painel
- <s>Fazer deploy na infra da JF</s>

Parte escrita (em .tex):

Antes de compilar os arquivos, lembre de executar os passos abaixo no console para garantir que o idioma e os pacotes estão instalados, lembrando que tudo feito aqui foi usando o Ubuntu 20.04

```console
sudo apt -y install texlive-lang-portuguese
sudo apt-get install texlive-full
```

<s>Vai ser fácil!</s>
