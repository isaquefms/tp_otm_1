"""
Este arquivo tem a finalidade de gerar as matrizes de custos para rodarmos as heurísticas para solução do problema de
atribuição de salas.
A lógica de montagem da matriz é a seguinte: temos dois subcustos, causados pelas restrições 3 e 4 do problema, conforme
descritas no artigo. O primeiro subcusto trata da capacidade da sala em relação à quantidade de alunos na turma. Chamamos
de cj. O segundo subcusto trata da distância da sala em relação ao ponto de referência. Chamamos de dj. cj é uma matriz
n x m e dj é uma lista de tamanho m, onde n é a quantidade de turmas e m é a quantidade de salas. Cada valor de dj repre-
senta a distancia da sala j até o ponto de referência. Após calcularmos cj e dj, adicionamos a cada linha de cj, a lista
dj. Usamos também um peso para a capacidade da sala x tamanho da turma e um outro peso para a distancia entre as salas e
o ponto de referencia. Este peso permite ao usuário definir qual dos dois subcustos deve ser o mais importante a se levar
em consideração para a montagem da matriz de custos.
"""
from typing import List


def set_capacity_restriction_costs(turmas: List[int], salas: List[int], peso_capacidade: float) -> List[List[float]]:
    """
    Define cj, ou seja, a matriz de subcustos que relaciona a atribuição de uma turma a uma sala levando em consideração
    a capacidade da sala e o tamanho da turma. Caso o tamanho da turma seja maior que a capacidade da sala, atribuimos
    um valor muito alto, ou seja, 1. Caso contrário, atribuimos um valor pequeno, que aumenta linearmente com a diferença
    entre estes dois valores. Desta forma, quanto mais próximo for o tamanho da turma da capacidade da sala, menor será
    o seu custo, e portanto, a probabilidade de escolha desta atribuição será maior.
    :param turmas: lista de tamanhos das turmas
    :param salas: lista das capacidades das salas
    :param peso_capacidade: peso deste subcusto (importância desta restrição)
    :return: matriz de subcustos
    """
    probabilidades = list()
    for i, tamanho_turma in enumerate(turmas):
        probabilidades.append([])
        for capacidade_sala in salas:
            if capacidade_sala < tamanho_turma:
                probabilidades[i].append(1 * peso_capacidade)
            else:
                probabilidades[i].append((1 - (tamanho_turma / capacidade_sala)) * peso_capacidade)
    return probabilidades


def set_distance_restriction_costs(distancias, peso_distancia):
    """
    Define dj, ou seja, a lista de subcustos que relaciona a distancia entre cada sala e o ponto de referencia. Cada
    distancia é normalizada para entregar um valor entre 0 e 1, e multiplicada pelo peso informado pelo usuário.
    :param distancias: lista de distâncias
    :param peso_distancia: peso deste subcusto (importância desta restrição)
    :return: lista de subcustos
    """
    d_total = 0
    distancias_normalizadas = []
    for distancia in distancias:
        d_total += distancia
    for distancia in distancias:
        distancias_normalizadas.append((distancia / d_total) * peso_distancia)
    return distancias_normalizadas


def def_costs_matrix(turmas, salas, distancias, peso_capacidade, peso_distancia):
    """
    Define a matriz de custos com base nos subcustos cj e dj. A lista dj é adicionada a cada linha da matriz cj.
    :param turmas: lista de tamanhos das turmas
    :param salas: lista das capacidades das salas
    :param peso_capacidade: peso deste subcusto (importância desta restrição)
    :param distancias: lista de distâncias
    :param peso_distancia: peso deste subcusto (importância desta restrição)
    :return: matriz de custos
    """
    cj = set_capacity_restriction_costs(turmas, salas, peso_capacidade)
    dj = set_distance_restriction_costs(distancias, peso_distancia)
    for i, linha in enumerate(cj):
        for j, _ in enumerate(linha):
            cj[i][j] += dj[j]
    return cj


def main():
    """
    Executa o algoritmo de construção da matriz de custos
    :return:
    """
    print(def_costs_matrix([35, 26, 21, 45, 40, 37, 23, 28, 19, 36], [27, 17, 36, 18, 39, 16, 28, 24, 19, 33],
                           [260, 211, 334, 263, 282, 315, 262, 387, 218, 367], 0.9, 0.1))


main()  # chama a função de execução
