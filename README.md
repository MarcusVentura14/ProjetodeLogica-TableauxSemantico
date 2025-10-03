# Tableau Semântico 

    O Tableaux Semântico ou Árvore de Refutação é um método de prova que supõe as premissas de um sequente como verdadeiras e as conclusões como falsas buscando encontrar uma contradição para todos os cenários de valoração possíveis(isto é, para todos os ramos da árvore de possibilidades lógicas) com o fim de mostrar que a suposição inicial é impossível (funcionando como uma espécie de prova por contradição).

# Estratégias Computacionais

    Dentre as estratégias computacionais possíveis para a implementação do Tableaux, o algoritmo fornecido utiliza a Busca em Profundidade (Depth-First Search - DFS) como método de travessia da árvore de prova, otimizando cada passo ao priorizar as regras de expansão que não criam novas ramificações (regras alfa).

## Como o Algoritmo usa DFS

    A Busca em Profundidade (DFS) é um clássico algoritmo de percurso em grafos ou árvores que busca explorar cada ramo o mais profundamente possível avançando de um vértice para um de seus vizinhos ainda não visitados até encontrar um vértice que não tenha vizinhos não visitados (momento em que se retorna ao vértice anterior para se explorar novas ramificações).

    O algoritmo implementado utiliza a estratégia de busca em profundidade (DFS), ao armazenar e operar sobre apenas um ramo do tableau por vez, contido na variável ramo_atual. No loop "while true", expande-se o ramo até que ele se feche por contradição ou se sature (encontrando um contraexemplo). O modo como o código realiza o "backtracking", após prosseguir a busca com o primeiro resultado da bifurcação de uma fórmula beta e esse caminho fechar, se dá por meio da implementação da pilha de ramos, que ao guardar o caminho até antes da bifurcação junto com o segundo resultado, permite que se explore o caminho alternativo.

## Estratégia de Seleção de Regras

    Em busca de maior eficiência e otimização no desenvolvimento de cada ramo, prioriza-se a aplicação de regras alfa para que o algoritmo encontre contradições de maneira mais rápida e econômica, evitando, assim, ramificações desnecessárias. 
    
    Essa estratégia se reflete no código quando a busca pela próxima fórmula a ser expandida começa na tentativa de encontrar fórmulas alfas não expandidas primeiro. Só depois, caso "proxima_formula_para_expandir" seja "None" (não foi encontrada nenhuma fórmula alfa), um segundo loop é executado para buscar fórmulas beta. 



    

  
