"""
10 turmas (i): [23, 14, 30, 24, 35, 40, 43, 19, 36, 15]
10 salas (j): [25, 25, 25, 40, 45, 20, 15, 20, 35, 35]
10 distancias (d): [292, 221, 206, 181, 219, 103, 164, 141, 220, 251]
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
    print(def_costs_matrix([23, 14, 30, 24, 35, 40, 43, 19, 36, 15], [25, 25, 25, 40, 45, 20, 15, 20, 35, 35],
                           [292, 221, 206, 181, 219, 103, 164, 141, 220, 251], 0.9, 0.1))


main()
