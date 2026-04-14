# -*- coding: utf-8 -*-
# SCRIPT 04: WAYPOINTS REPETIDOS
# Autor: Diego Hector Maraboli | Fecha: 2026-04-15

from collections import defaultdict
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
    ab = int(s[:2])
    return (ab - 100 if ab > 90 else ab, int(s[2:4]) + int(s[4])/10)

def main():
    frec = defaultdict(list)
    for i, bloque in enumerate(CIFRADO, 1):
        frec[bloque].append(i)
    repetidos = {k: v for k, v in frec.items() if len(v) > 1}
    print(f'Total: {len(CIFRADO)} | Unicas: {len(frec)} | Repetidas: {len(repetidos)}')
    for bloque, indices in sorted(repetidos.items()):
        lat, lon = decodificar(bloque)
        print(f'{bloque}: {lat}°, {lon}°E | Pos: {indices}')
    with open('resultados_waypoints.json', 'w') as f:
        json.dump({'waypoints': list(repetidos.keys())}, f)

if __name__ == '__main__':
    main()
