[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FRA0NLo8)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=14112907)
# Lab01

Neste lab, construa as implementações indicadas abaixo.

**Observações Gerais:**

* Não altere a estrutura do repositório ou modifique nomes dos arquivos ou folders;

* Não altere arquivos da pasta test ou workflows;

* Não altere os nomes das variáveis que definem os autômatos solicitados, visto que esta atividade será avaliada através de testes automáticos;

* As soluções devem ser implementadas exclusivamente usando a biblioteca automata-lib

Entrega:

* Realizar push com a versão final do repositório;
* Confira o status da execução automática dos testes na aba Actions no GitHub;
* Caso seu projeto contenha algum erro de compilação, nenhum teste será executado e, portanto, não poderá ser corrigido;

## Questão 01

Implemente um DFA que reconhece a linguagem descrita por $(ab)^+$.
Como exemplo, as palavras $ab$ e $ababab$ fazem parte desta linguagem.

Arquivos: 
* src/Q01.py (local onde o dfa deve ser definido)
* test/test_Q01.py

Execução dos testes automáticos: 

   python -m unittest -v test/test_Q01.py

## Questão 02

Implemente um NFA que reconhece a linguagem descrita por  $(0^∗1^∗)|(1^∗0^∗)$.
Como exemplo, as palavras $\epsilon$ e $110$ fazem parte desta linguagem.

Arquivos: 
* src/Q02.py (local onde o nfa deve ser definido)
* test/test_Q02.py

Execução dos testes automáticos: 

   python -m unittest -v test/test_Q02.py


## Questão 03

Implemente as expressões regulares das questões 01 e 02 no formato da biblioteca [re](https://docs.python.org/3/library/re.html) de python. Use o trecho de código do repositório (main_re.py) para teste manual.

Para esta questão e para questões correspondentes no EP01, é necessário compreender apenas alguns construtores de re. São eles:

* `*` - Kleene star. ab* corresponderá a ‘a’, ‘ab’ ou ‘a’ seguido por qualquer número de ‘b’s.

* `+` - Uma ou mais repetições. ab+ corresponderá a ‘a’ seguido por qualquer número diferente de zero de ‘b’; não corresponderá apenas a 'a'.

* `[]` - Indica um conjunto de caracteres onde um deles pode ser selecionado. Exemplos: [a-z], [ab_]

* `|` - A|B, onde A e B podem ser REs arbitrárias; cria uma expressão regular que corresponderá a A ou B

* `(...)` - Agrupamento de expressões

* `\b` - cadeia vazia

* `\s` - caracter espaço em branco

* `\<caracter especial>` - representação de caracteres reservados, como `.` `+` `-`. Ex: `\.`
