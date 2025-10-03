# Tableau Semântico 

    O Tableaux Semântico ou Árvore de Refutação é um método de prova que supõe as premissas de um sequente como verdadeiras e as conclusões como falsas buscando encontrar uma contradição para todos os cenários de valoração possíveis(isto é, para todos os ramos da árvore de possibilidades lógicas) com o fim de mostrar que a suposição inicial é impossível (funcionando como uma espécie de prova por contradição).

# Estratégias Computacionais

    Dentre as estratégias computacionais possíveis para a implementação do Tableaux, o algoritmo fornecido utiliza a Busca em Profundidade (Depth-First Search - DFS) como método de travessia da árvore de prova, otimizando cada passo ao priorizar as regras de expansão que não criam novas ramificações (regras alfa).

## Como o Algoritmo usa DFS

    A Busca em Profundidade (DFS) é um clássico algoritmo de percurso em grafos ou árvores que busca explorar cada ramo o mais profundamente possível avançando de um vértice para um de seus vizinhos ainda não visitados até encontrar um vértice que não tenha vizinhos não visitados (momento em que se retorna ao vértice anterior para se explorar novas ramificações).

    O algoritmo implementado utiliza a estratégia de busca em profundidade (DFS), ao armazenar e operar sobre apenas um ramo do tableau por vez, contido na variável "ramo_atual". No loop "while true", expande-se o ramo até que ele se feche por contradição ou se sature (encontrando um contraexemplo). O modo como o código realiza o "backtracking", após prosseguir a busca com o primeiro resultado da bifurcação de uma fórmula beta e esse caminho fechar, se dá por meio da implementação da pilha de ramos, que ao guardar o caminho até antes da bifurcação junto com o segundo resultado, permite que se explore o caminho alternativo.

## Estratégia de Seleção de Regras

    Em busca de maior eficiência e otimização no desenvolvimento de cada ramo, prioriza-se a aplicação de regras alfa para que o algoritmo encontre contradições de maneira mais rápida e econômica, evitando, assim, ramificações desnecessárias. 
    
    Essa estratégia se reflete no código quando a busca pela próxima fórmula a ser expandida começa na tentativa de encontrar fórmulas alfas não expandidas primeiro. Só depois, caso "proxima_formula_para_expandir" seja "None" (não foi encontrada nenhuma fórmula alfa), um segundo loop é executado para buscar fórmulas beta. 

# Breve Descrição do Código

## Representação das Fórmulas

    A implementação da função principal "tableaux" se fundamenta sobre dois pilares: as fórmulas lógicas assinaladas e as regras de derivação que a elas se aplicam. O código, portanto, começa pela estrutração das fórmulas lógicas por meio de classes (Atomica, Nao, E, Ou, Implica) com suas devidas valorações (FormulaAssinalada). Há também, inicialmente, a definição das regras de expansão dos ramos de acordo com o tipo de fórmula (alfa ou beta) por meio da função "expansao_da_fórmula". 

## O algoritmo Tableaux

    Inicialização:
     O estágio de inicialização da árvore começa com a valoraração das premissas (T) e conclusões (F) e com a criação da pilha de ramos (estrutura essencial para a DFS).

    Loop Principal e Busca por Contradições:
     Concluído a inicialização, o programa parte para a busca de contradições no ramo atual para fechá-lo, verificação que sempre ocorre no início da análise de um novo ramo para evitar ramificações desnecessárias. 

    Contradição Encontrada e Backtracking:
     Se há contradição, a pilha de ramos (que armazenará os caminhos alternativos a serem percorridos) é a referência para a conclusão de que apenas um ramo fechou ou todos os ramos possíveis fecharam (e, por consequência o tableaux). Se a pilha estiver vazia e o ramo fechou então junto com ele o tableaux e o programa encerra (o sequente é válido), de outro modo, se a pilha não está vazia, o caminho alternativo mais recente é restaurado e a busca continua.

    Seleção e Aplicação de Regras:
     Se não há contradição, o algoritmo busca a próxima ramificação priorizando a expansão de fórmulas alfa em detrimento das fórmulas beta. A regra correspondente é, assim, aplicada, adicionando novas fórmulas ao ramo atual ou, no caso de uma regra beta, criando uma bifurcação (onde um caminho é explorado e o outro é guardado na pilha).

    Término com Ramo Aberto: Realizadas todas as expansões possíveis de cada fórmula do ramo e ainda não há contradição, concluí-se que o ramo está saturado e aberto, sendo oferecido um contra-exemplo com as fómulas atômicas presentes no ramo.
    
## Interpretando os Resultados
     
    O contra-exemplo é o que mostra que a prova do sequente não se sustenta, já que há, de fato, um cenário de valoração possível para as fórmulas atômicas das premissas que resulta na validade da negação da valoração das conclusões (afirmação que pretende-se provar que é impossível, mas que se mostra verdadeira). 
    
    Quando o tableaux se fecha para todos os ramos, temos a prova de que em todos os cenários de valoração possíveis a afirmação de premissas como verdadeiras e conclusões como falsas é um absurdo o que mostra que é verdadeiro o sequente.


     


    

  
