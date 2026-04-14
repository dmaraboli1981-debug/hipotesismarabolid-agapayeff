# -*- coding: utf-8 -*-
# SCRIPT 03: VALIDACION CRUZADA 50/50
# Autor: Diego Hector Maraboli | Fecha: 2026-04-15

import numpy as np
from sklearn.model_selection import train_test_split
import json

CIFRADO = [75628, 28591, 62916, 48164, 91748, 58464, 74748, 28483, 81638, 18174,
    74826, 26475, 83828, 49175, 74658, 37575, 75936, 36565, 81638, 17585,
    75756, 46282, 92857, 46382, 75748, 38165, 81848, 56485, 64858, 56382,
    72628, 36281, 81728, 16463, 75828, 16483, 63828, 58163, 63630, 47481,
    91918, 46385, 84656, 48565, 62946, 26285, 91859, 17491, 72756, 46575,
    71658, 36264, 74818, 28462, 82649, 18193, 65626, 48484, 91838, 57491,
    81657, 27483, 83858, 28364, 62726, 26562, 83759, 27263, 82827, 27283,
    82858, 47582, 81837, 28462, 82837, 58164, 75748, 58162]

def decodificar(b):
    s = str(b).zfill(5)
    return (int(s[:2]) - 100 if int(s[:2]) > 90 else int(s[:2]), 
            int(s[2:4]) + int(s[4])/10)

def es_rie(lat, lon):
    return ((70 <= abs(lat) <= 85 and 60 <= lon <= 95) or
            (25 <= abs(lat) <= 30 and 47 <= lon <= 55) or
            (55 <= abs(lat) <= 60 and 10 <= lon <= 20))

def calcular_ice(coords):
    return sum(1 for lat, lon in coords if es_rie(lat, lon)) / len(coords) * 100

def main():
    coords = [decodificar(b) for b in CIFRADO]
    test_scores = []
    for i in range(1000):
        train_idx, test_idx = train_test_split(range(78), test_size=0.5, random_state=2026+i)
        test_scores.append(calcular_ice([coords[j] for j in test_idx]))
    pct = sum(1 for s in test_scores if s > 40) / len(test_scores) * 100
    print(f'% Test > 40%: {pct:.1f}%')
    print('SIN OVERFITTING' if pct > 95 else 'REVISAR')
    with open('resultados_validacion.json', 'w') as f:
        json.dump({'pct': pct}, f)

if __name__ == '__main__':
    main()
