"""
10 turmas (i): [15, 22, 45, 30, 42, 40, 15, 28, 33, 28]
10 salas (j): [36, 27, 35, 35, 39, 39, 25, 34, 36, 21]
10 distancias (d): [237, 153, 297, 348, 346, 192, 224, 269, 161, 287]
"""


def set_capacity_restriction_costs(turmas, salas, peso_capacidade):
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
    d_total = 0
    distancias_normalizadas = []
    for distancia in distancias:
        d_total += distancia
    for distancia in distancias:
        distancias_normalizadas.append((distancia / d_total) * peso_distancia)
    return distancias_normalizadas


def def_costs_matrix(turmas, salas, distancias, peso_capacidade, peso_distancia):
    cj = set_capacity_restriction_costs(turmas, salas, peso_capacidade)
    dj = set_distance_restriction_costs(distancias, peso_distancia)
    for i, linha in enumerate(cj):
        for j, _ in enumerate(linha):
            cj[i][j] += dj[j]
    return cj


def main():
    print(def_costs_matrix([15, 22, 45, 30, 42, 40, 15, 28, 33, 28], [36, 27, 35, 35, 39, 39, 25, 34, 36, 21],
                           [237, 153, 297, 348, 346, 192, 224, 269, 161, 287], 0.9, 0.1))


main()
