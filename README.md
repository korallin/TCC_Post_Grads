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

- Estudar os códigos das estudantes de Iniciação Científica do Professor Elias
- Terminar o curso de PostgreSQL da Udemy
- Pesquisar materiais de criação de Dashboards usando Python

<s>Vai ser fácil!</s>
