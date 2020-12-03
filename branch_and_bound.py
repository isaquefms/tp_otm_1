import time

from typing import List
from instancias import matriz_de_custos_1, matriz_de_custos_2, \
    matriz_de_custos_3, matriz_de_custos_4, matriz_de_custos_5, \
    matriz_de_custos_6, matriz_de_custos_7, matriz_de_custos_8, \
    matriz_de_custos_9, matriz_de_custos_10


def branch_and_bound(m_costs: List[List[float]]) -> List[tuple]:
    """Dado uma matriz de custos calcula uma solução usando o algoritmo
    brench and bound.

    Args:
        m_costs: Matriz de custos.

    Returns: Lista com as tuplas (i, j) que definem a atribuição de uma
    determinada turma i a uma sala j.
    """
    # conjuntos de linhas e colunas já selecionados em uma solução
    linhas_visitadas = set()
    colunas_visitadas = set()
    resultado = []
    custo_total = 0

    # iterando sobre cada disciplina da matriz de custos
    for i, linha in enumerate(m_costs):
        linhas_visitadas.add(i)  # marcamos a linha como visitada
        menor_valor = 1000  # valor fictício de inicialização
        coluna_do_menor_valor = 0  # inicializando
        for j, valor in enumerate(linha):
            # se j não estiver dentre as colunas visitadas podemos conferi-la
            if j not in colunas_visitadas:
                if valor < menor_valor:
                    menor_valor = valor
                    coluna_do_menor_valor = j
        # somando o custo atual ao custo total
        custo_total += menor_valor
        # ao terminar de se verificar a linha teremos o menor valor
        resultado.append((i, coluna_do_menor_valor))  # (disciplina, sala)
        # marcamos o índice da coluna como uma coluna visitada
        colunas_visitadas.add(coluna_do_menor_valor)
    # retornando o resultado
    return resultado, custo_total


def main():
    # instância 1
    inicio_1 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_1)
    fim_1 = time.time()
    total_1 = fim_1 - inicio_1
    print(f'1: Solucao: {solucao}, custo: {custo} e tempo: {total_1}')
    print()
    # instância 2
    inicio_2 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_2)
    fim_2 = time.time()
    total_2 = fim_2 - inicio_2
    print(f'2: Solucao: {solucao}, custo: {custo} e tempo: {total_2}')
    print()
    # instância 3
    inicio_3 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_3)
    fim_3 = time.time()
    total_3 = fim_3 - inicio_3
    print(f'3: Solucao: {solucao}, custo: {custo} e tempo: {total_3}')
    print()
    # instância 4
    inicio_4 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_4)
    fim_4 = time.time()
    total_4 = fim_4 - inicio_4
    print(f'4: Solucao: {solucao}, custo: {custo} e tempo: {total_4}')
    print()
    # instância 5
    inicio_5 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_5)
    fim_5 = time.time()
    total_5 = fim_5 - inicio_5
    print(f'5: Solucao: {solucao}, custo: {custo} e tempo: {total_5}')
    print()
    # instância 6
    inicio_6 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_6)
    fim_6 = time.time()
    total_6 = fim_6 - inicio_6
    print(f'6: Solucao: {solucao}, custo: {custo} e tempo: {total_6}')
    print()
    # instância 7
    inicio_7 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_7)
    fim_7 = time.time()
    total_7 = fim_7 - inicio_7
    print(f'7: Solucao: {solucao}, custo: {custo} e tempo: {total_7}')
    print()
    # instância 8
    inicio_8 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_8)
    fim_8 = time.time()
    total_8 = fim_8 - inicio_8
    print(f'8: Solucao: {solucao}, custo: {custo} e tempo: {total_8}')
    print()
    # instância 9
    inicio_9 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_9)
    fim_9 = time.time()
    total_9 = fim_9 - inicio_9
    print(f'9: Solucao: {solucao}, custo: {custo} e tempo: {total_9}')
    print()
    # instância 10
    inicio_10 = time.time()
    solucao, custo = branch_and_bound(matriz_de_custos_10)
    fim_10 = time.time()
    total_10 = fim_10 - inicio_10
    print(f'10: Solucao: {solucao}, custo: {custo} e tempo: {total_10}')
    print()


main()
