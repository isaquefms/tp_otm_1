# Método Húngaro - Soluções

# Instância 01

# tamanhos_turmas = [23, 14, 30, 24, 35, 40, 43, 19, 36, 15]

# capacidade_salas = [25, 25, 25, 40, 45, 20, 15, 20, 35, 35]

# distancias = [292, 221, 206, 181, 219, 103, 164, 141, 220, 251]

matriz_de_custos_1 = [
    [0.0866, 0.0830, 0.0823, 0.3915, 0.4509, 0.9051, 0.9082, 0.9070, 0.3195,
        0.3211],
    [0.4106, 0.4070, 0.4063, 0.5940, 0.6309, 0.2751, 0.0682, 0.2770, 0.5510,
        0.5525],
    [0.9146, 0.9110, 0.9103, 0.2340, 0.3109, 0.9051, 0.9082, 0.9070, 0.1395,
        0.1411],
    [0.0506, 0.0470, 0.0463, 0.3690, 0.4309, 0.9051, 0.9082, 0.9070, 0.2938,
        0.2954],
    [0.9146, 0.9110, 0.9103, 0.1215, 0.2109, 0.9051, 0.9082, 0.9070, 0.0110,
        0.0125],
    [0.9146, 0.9110, 0.9103, 0.0090, 0.1109, 0.9051, 0.9082, 0.9070, 0.9110,
        0.9125],
    [0.9146, 0.9110, 0.9103, 0.9090, 0.0509, 0.9051, 0.9082, 0.9070, 0.9110,
        0.9125],
    [0.2306, 0.2270, 0.2263, 0.4815, 0.5309, 0.0501, 0.9082, 0.0520, 0.4224,
        0.4239],
    [0.9146, 0.9110, 0.9103, 0.0990, 0.1909, 0.9051, 0.9082, 0.9070, 0.9110,
        0.9125],
    [0.3746, 0.3710, 0.3703, 0.5715, 0.6109, 0.2301, 0.0082, 0.2320, 0.5252,
        0.5268]]


# Instância 02

# tamanhos_turmas = [26, 44, 26, 37, 26, 33, 38, 24, 18, 34]

# capacidade_salas = [18, 22, 29, 15, 34, 22, 35, 24, 45, 19]

# distancias = [214, 246, 248, 259, 163, 223, 243, 340, 310, 330]

matriz_de_custos_2 = [
    [0.9083, 0.9095, 0.1027, 0.9100, 0.2180, 0.9086, 0.2408, 0.9131, 0.3920,
        0.9128],
    [0.9083, 0.9095, 0.9096, 0.9100, 0.9063, 0.9086, 0.9094, 0.9131, 0.0320,
        0.9128],
    [0.9083, 0.9095, 0.1027, 0.9100, 0.2180, 0.9086, 0.2408, 0.9131, 0.3920,
        0.9128],
    [0.9083, 0.9095, 0.9096, 0.9100, 0.9063, 0.9086, 0.9094, 0.9131, 0.1720,
        0.9128],
    [0.9083, 0.9095, 0.1027, 0.9100, 0.2180, 0.9086, 0.2408, 0.9131, 0.3920,
        0.9128],
    [0.9083, 0.9095, 0.9096, 0.9100, 0.0327, 0.9086, 0.0608, 0.9131, 0.2520,
        0.9128],
    [0.9083, 0.9095, 0.9096, 0.9100, 0.9063, 0.9086, 0.9094, 0.9131, 0.1520,
        0.9128],
    [0.9083, 0.9095, 0.1647, 0.9100, 0.2710, 0.9086, 0.2922, 0.0131, 0.4320,
        0.9128],
    [0.0083, 0.1731, 0.3510, 0.9100, 0.4298, 0.1722, 0.4465, 0.2381, 0.5520,
        0.0601],
    [0.9083, 0.9095, 0.9096, 0.9100, 0.0063, 0.9086, 0.0351, 0.9131, 0.2320,
        0.9128]]


# Instância 03

# tamanhos_turmas = [19, 32, 30, 32, 41, 40, 25, 21, 26, 35]

# capacidade_salas = [16, 27, 27, 40, 35, 42, 27, 43, 28, 30]

# distancias = [175, 189, 161, 164, 209, 312, 230, 233, 204, 327]

matriz_de_custos_3 = [
    [0.9079, 0.2752, 0.2739, 0.4799, 0.4209, 0.5070, 0.2771, 0.5128, 0.2985,
        0.3448],
    [0.9079, 0.9085, 0.9073, 0.1874, 0.0866, 0.2284, 0.9104, 0.2408, 0.9092,
        0.9148],
    [0.9079, 0.9085, 0.9073, 0.2324, 0.1380, 0.2712, 0.9104, 0.2826, 0.9092,
        0.0148],
    [0.9079, 0.9085, 0.9073, 0.1874, 0.0866, 0.2284, 0.9104, 0.2408, 0.9092,
        0.9148],
    [0.9079, 0.9085, 0.9073, 0.9074, 0.9094, 0.0355, 0.9104, 0.0524, 0.9092,
        0.9148],
    [0.9079, 0.9085, 0.9073, 0.0074, 0.9094, 0.0570, 0.9104, 0.0733, 0.9092,
        0.9148],
    [0.9079, 0.0752, 0.0739, 0.3449, 0.2666, 0.3784, 0.0771, 0.3873, 0.1056,
        0.1648],
    [0.9079, 0.2085, 0.2073, 0.4349, 0.3694, 0.4641, 0.2104, 0.4710, 0.2342,
        0.2848],
    [0.9079, 0.0419, 0.0406, 0.3224, 0.2409, 0.3570, 0.0437, 0.3663, 0.0735,
        0.1348],
    [0.9079, 0.9085, 0.9073, 0.1199, 0.0094, 0.1641, 0.9104, 0.1780, 0.9092,
        0.9148]]

# Instância 04

# tamanhos_turmas = [15, 22, 45, 30, 42, 40, 15, 28, 33, 28]

# capacidade_salas = [36, 27, 35, 35, 39, 39, 25, 34, 36, 21]

# distancias = [237, 153, 297, 348, 346, 192, 224, 269, 161, 287]

matriz_de_custos_4 = [
    [0.5344, 0.4060, 0.5260, 0.5281, 0.5676, 0.5614, 0.3689, 0.5136, 0.5314,
        0.2685],
    [0.3594, 0.1727, 0.3460, 0.3481, 0.4060, 0.3999, 0.1169, 0.3283, 0.3564,
        0.9114],
    [0.9094, 0.9060, 0.9118, 0.9138, 0.9137, 0.9076, 0.9089, 0.9107, 0.9064,
        0.9114],
    [0.1594, 0.9060, 0.1403, 0.1424, 0.2214, 0.2153, 0.9089, 0.1165, 0.1564,
        0.9114],
    [0.9094, 0.9060, 0.9118, 0.9138, 0.9137, 0.9076, 0.9089, 0.9107, 0.9064,
        0.9114],
    [0.9094, 0.9060, 0.9118, 0.9138, 0.9137, 0.9076, 0.9089, 0.9107, 0.9064,
        0.9114],
    [0.5344, 0.4060, 0.5260, 0.5281, 0.5676, 0.5614, 0.3689, 0.5136, 0.5314,
        0.2685],
    [0.2094, 0.9060, 0.1918, 0.1938, 0.2676, 0.2614, 0.9089, 0.1695, 0.2064,
        0.9114],
    [0.0844, 0.9060, 0.0632, 0.0652, 0.1522, 0.1460, 0.9089, 0.0371, 0.0814,
        0.9114],
    [0.2094, 0.9060, 0.1918, 0.1938, 0.2676, 0.2614, 0.9089, 0.1695, 0.2064,
        0.9114]]

# Instância 05

# tamanhos_turmas = [34, 30, 31, 28, 37, 31, 41, 35, 41, 31]

# capacidade_salas = [18, 22, 27, 31, 20, 22, 29, 19, 44, 45]

# distancias = [162, 190, 167, 428, 370, 330, 361, 371, 188, 321]

matriz_de_custos_5 = [
    [0.9056, 0.9065, 0.9057, 0.9148, 0.9128, 0.9114, 0.9125, 0.9128, 0.2110,
        0.2311],
    [0.9056, 0.9065, 0.9057, 0.0438, 0.9128, 0.9114, 0.9125, 0.9128, 0.2928,
        0.3111],
    [0.9056, 0.9065, 0.9057, 0.0148, 0.9128, 0.9114, 0.9125, 0.9128, 0.2724,
        0.2911],
    [0.9056, 0.9065, 0.9057, 0.1019, 0.9128, 0.9114, 0.0435, 0.9128, 0.3337,
        0.3511],
    [0.9056, 0.9065, 0.9057, 0.9148, 0.9128, 0.9114, 0.9125, 0.9128, 0.1496,
        0.1711],
    [0.9056, 0.9065, 0.9057, 0.0148, 0.9128, 0.9114, 0.9125, 0.9128, 0.2724,
        0.2911],
    [0.9056, 0.9065, 0.9057, 0.9148, 0.9128, 0.9114, 0.9125, 0.9128, 0.0678,
        0.0911],
    [0.9056, 0.9065, 0.9057, 0.9148, 0.9128, 0.9114, 0.9125, 0.9128, 0.1906,
        0.2111],
    [0.9056, 0.9065, 0.9057, 0.9148, 0.9128, 0.9114, 0.9125, 0.9128, 0.0678,
        0.0911],
    [0.9056, 0.9065, 0.9057, 0.0148, 0.9128, 0.9114, 0.9125, 0.9128, 0.2724,
        0.2911]]

# Instância 06

# tamanhos_turmas = [33, 30, 34, 17, 18, 21, 45, 31, 38, 22]

# capacidade_salas = [36, 16, 32, 32, 45, 41, 16, 38, 42, 29]

# distancias = [386, 360, 286, 304, 345, 277, 219, 385, 193, 375]

matriz_de_custos_6 = [
    [0.0873, 0.9115, 0.9091, 0.9097, 0.2510, 0.1844, 0.9069, 0.1307, 0.1990,
        0.9119],
    [0.1623, 0.9115, 0.0653, 0.0659, 0.3110, 0.2503, 0.9069, 0.2017, 0.2633,
        0.9119],
    [0.0623, 0.9115, 0.9091, 0.9097, 0.2310, 0.1625, 0.9069, 0.1070, 0.1775,
        0.9119],
    [0.4873, 0.9115, 0.4310, 0.4315, 0.5710, 0.5356, 0.9069, 0.5096, 0.5418,
        0.3843],
    [0.4623, 0.9115, 0.4028, 0.4034, 0.5510, 0.5137, 0.9069, 0.4859, 0.5204,
        0.3533],
    [0.3873, 0.9115, 0.3185, 0.3190, 0.4910, 0.4478, 0.9069, 0.4149, 0.4561,
        0.2602],
    [0.9123, 0.9115, 0.9091, 0.9097, 0.0110, 0.9088, 0.9069, 0.9123, 0.9061,
        0.9119],
    [0.1373, 0.9115, 0.0372, 0.0378, 0.2910, 0.2283, 0.9069, 0.1780, 0.2418,
        0.9119],
    [0.9123, 0.9115, 0.9091, 0.9097, 0.1510, 0.0747, 0.9069, 0.0123, 0.0918,
        0.9119],
    [0.3623, 0.9115, 0.2903, 0.2909, 0.4710, 0.4259, 0.9069, 0.3912, 0.4347,
        0.2292]]

# Instância 07

# tamanhos_turmas = [40, 30, 31, 22, 41, 39, 18, 36, 27, 22]

# capacidade_salas = [24, 30, 17, 31, 45, 36, 45, 30, 35, 43]

# distancias = [406, 230, 404, 170, 328, 220, 268, 202, 354, 381]

matriz_de_custos_7 = [
    [0.9137, 0.9077, 0.9136, 0.9057, 0.1110, 0.9074, 0.1090, 0.9068, 0.9119,
        0.0756],
    [0.9137, 0.0077, 0.9136, 0.0347, 0.3110, 0.1574, 0.3090, 0.0068, 0.1405,
        0.2849],
    [0.9137, 0.9077, 0.9136, 0.0057, 0.2910, 0.1324, 0.2890, 0.9068, 0.1148,
        0.2640],
    [0.0887, 0.2477, 0.9136, 0.2670, 0.4710, 0.3574, 0.4690, 0.2468, 0.3462,
        0.4523],
    [0.9137, 0.9077, 0.9136, 0.9057, 0.0910, 0.9074, 0.0890, 0.9068, 0.9119,
        0.0547],
    [0.9137, 0.9077, 0.9136, 0.9057, 0.1310, 0.9074, 0.1290, 0.9068, 0.9119,
        0.0965],
    [0.2387, 0.3677, 0.9136, 0.3831, 0.5510, 0.4574, 0.5490, 0.3668, 0.4490,
        0.5361],
    [0.9137, 0.9077, 0.9136, 0.9057, 0.1910, 0.0074, 0.1890, 0.9068, 0.9119,
        0.1593],
    [0.9137, 0.0977, 0.9136, 0.1218, 0.3710, 0.2324, 0.3690, 0.0968, 0.2176,
        0.3477],
    [0.0887, 0.2477, 0.9136, 0.2670, 0.4710, 0.3574, 0.4690, 0.2468, 0.3462,
        0.4523]]

# Instância 08

# tamanhos_turmas = [35, 26, 21, 45, 40, 37, 23, 28, 19, 36]

# capacidade_salas = [27, 17, 36, 18, 39, 16, 28, 24, 19, 33]

# distancias = [260, 211, 334, 263, 282, 315, 262, 387, 218, 367]

matriz_de_custos_8 = [
    [0.9089, 0.9072, 0.0365, 0.9090, 0.1020, 0.9108, 0.9090, 0.9133, 0.9075,
        0.9126],
    [0.0423, 0.9072, 0.2615, 0.9090, 0.3097, 0.9108, 0.0733, 0.9133, 0.9075,
        0.2035],
    [0.2089, 0.9072, 0.3865, 0.9090, 0.4251, 0.9108, 0.2340, 0.1258, 0.9075,
        0.3399],
    [0.9089, 0.9072, 0.9115, 0.9090, 0.9097, 0.9108, 0.9090, 0.9133, 0.9075,
        0.9126],
    [0.9089, 0.9072, 0.9115, 0.9090, 0.9097, 0.9108, 0.9090, 0.9133, 0.9075,
        0.9126],
    [0.9089, 0.9072, 0.9115, 0.9090, 0.0558, 0.9108, 0.9090, 0.9133, 0.9075,
        0.9126],
    [0.1423, 0.9072, 0.3365, 0.9090, 0.3789, 0.9108, 0.1697, 0.0508, 0.9075,
        0.2853],
    [0.9089, 0.9072, 0.2115, 0.9090, 0.2635, 0.9108, 0.0090, 0.9133, 0.9075,
        0.1490],
    [0.2756, 0.9072, 0.4365, 0.9090, 0.4712, 0.9108, 0.2983, 0.2008, 0.0075,
        0.3944],
    [0.9089, 0.9072, 0.0115, 0.9090, 0.0789, 0.9108, 0.9090, 0.9133, 0.9075,
        0.9126]]

# Instância 09

# tamanhos_turmas = [27, 39, 44, 21, 42, 42, 40, 41, 38, 25]

# capacidade_salas = [29, 24, 41, 28, 18, 35, 16, 27, 34, 17]

# distancias = [290, 336, 201, 159, 303, 416, 168, 211, 391, 230]

matriz_de_custos_9 = [
    [0.0727, 0.9124, 0.3147, 0.0380, 0.9112, 0.2210, 0.9062, 0.0078, 0.1997,
        0.9085],
    [0.9107, 0.9124, 0.0513, 0.9058, 0.9112, 0.9153, 0.9062, 0.9078, 0.9144,
        0.9085],
    [0.9107, 0.9124, 0.9074, 0.9058, 0.9112, 0.9153, 0.9062, 0.9078, 0.9144,
        0.9085],
    [0.2589, 0.1249, 0.4464, 0.2308, 0.9112, 0.3753, 0.9062, 0.2078, 0.3585,
        0.9085],
    [0.9107, 0.9124, 0.9074, 0.9058, 0.9112, 0.9153, 0.9062, 0.9078, 0.9144,
        0.9085],
    [0.9107, 0.9124, 0.9074, 0.9058, 0.9112, 0.9153, 0.9062, 0.9078, 0.9144,
        0.9085],
    [0.9107, 0.9124, 0.0293, 0.9058, 0.9112, 0.9153, 0.9062, 0.9078, 0.9144,
        0.9085],
    [0.9107, 0.9124, 0.0074, 0.9058, 0.9112, 0.9153, 0.9062, 0.9078, 0.9144,
        0.9085],
    [0.9107, 0.9124, 0.0732, 0.9058, 0.9112, 0.9153, 0.9062, 0.9078, 0.9144,
        0.9085],
    [0.1348, 0.9124, 0.3586, 0.1023, 0.9112, 0.2725, 0.9062, 0.0744, 0.2526,
        0.9085]]

# Instância 10

# tamanhos_turmas = [27, 28, 29, 27, 18, 37, 40, 41, 25, 22]

# capacidade_salas = [43, 24, 18, 42, 23, 43, 21, 32, 45, 16]

# distancias = [445, 308, 426, 356, 156, 401, 205, 208, 293, 312]

matriz_de_custos_10 = [
    [0.3491, 0.9099, 0.9136, 0.3328, 0.9050, 0.3477, 0.9065, 0.1473, 0.3694,
        0.9100],
    [0.3282, 0.9099, 0.9136, 0.3114, 0.9050, 0.3268, 0.9065, 0.1191, 0.3494,
        0.9100],
    [0.3073, 0.9099, 0.9136, 0.2900, 0.9050, 0.3059, 0.9065, 0.0910, 0.3294,
        0.9100],
    [0.3491, 0.9099, 0.9136, 0.3328, 0.9050, 0.3477, 0.9065, 0.1473, 0.3694,
        0.9100],
    [0.5375, 0.2349, 0.0136, 0.5257, 0.2006, 0.5361, 0.1351, 0.4004, 0.5494,
        0.9100],
    [0.1398, 0.9099, 0.9136, 0.1185, 0.9050, 0.1384, 0.9065, 0.9066, 0.1694,
        0.9100],
    [0.0770, 0.9099, 0.9136, 0.0543, 0.9050, 0.0756, 0.9065, 0.9066, 0.1094,
        0.9100],
    [0.0561, 0.9099, 0.9136, 0.0328, 0.9050, 0.0547, 0.9065, 0.9066, 0.0894,
        0.9100],
    [0.3910, 0.9099, 0.9136, 0.3757, 0.9050, 0.3896, 0.9065, 0.2035, 0.4094,
        0.9100],
    [0.4538, 0.0849, 0.9136, 0.4400, 0.0441, 0.4524, 0.9065, 0.2879, 0.4694,
        0.9100]]
