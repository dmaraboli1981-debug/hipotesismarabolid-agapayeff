# -*- coding: utf-8 -*-
# SCRIPT 01: DECODIFICACION MARABOLI Y CALCULO DEL ICE
# Autor: Diego Hector Maraboli | Fecha: 2026-04-15 | Version: 4.0

import numpy as np
import json
from dataclasses import dataclass
from datetime import datetime

__author__ = 'Diego Hector Maraboli'

CIFRADO_ORIGINAL = [
    75628, 28591, 62916, 48164, 91748, 58464, 74748, 28483, 81638, 18174,
    74826, 26475, 83828, 49175, 74658, 37575, 75936, 36565, 81638, 17585,
    75756, 46282, 92857, 46382, 75748, 38165, 81848, 56485, 64858, 56382,
    72628, 36281, 81728, 16463, 75828, 16483, 63828, 58163, 63630, 47481,
    91918, 46385, 84656, 48565, 62946, 26285, 91859, 17491, 72756, 46575,
    71658, 36264, 74818, 28462, 82649, 18193, 65626, 48484, 91838, 57491,
    81657, 27483, 83858, 28364, 62726, 26562, 83759, 27263, 82827, 27283,
    82858, 47582, 81837, 28462, 82837, 58164, 75748, 58162, 92000
]

@dataclass
class RIE:
    id: str
    nombre: str
    lat_min: float
    lat_max: float
    lon_min: float
    lon_max: float

RIE_DEFINICIONES = [
    RIE('RIE-1', 'Artico Sovietico', 70, 85, 60, 95),
    RIE('RIE-2', 'Concesiones Petroleras', 25, 30, 47, 55),
    RIE('RIE-3', 'Mar del Norte', 55, 60, 10, 20),
    RIE('RIE-4', 'Oceano Indico', -5, 10, 70, 95),
    RIE('RIE-5', 'Mediterraneo Oriental', 30, 40, 20, 35)
]

def decodificar_maraboli(bloque):
    s = str(bloque).zfill(5)
    ab = int(s[0:2])
    lat = ab - 100 if ab > 90 else ab
    lon = int(s[2:4]) + int(s[4]) / 10
    return lat, lon

def clasificar_rie(lat, lon):
    for rie in RIE_DEFINICIONES:
        if rie.lat_min <= abs(lat) <= rie.lat_max and rie.lon_min <= lon <= rie.lon_max:
            return rie.nombre
    return 'Otro'

def calcular_ice(coordenadas):
    en_rie = sum(1 for lat, lon in coordenadas if clasificar_rie(lat, lon) != 'Otro')
    return (en_rie / len(coordenadas)) * 100

def main():
    print('=' * 78)
    print('DECODIFICACION MARABOLI - CIFRADO DAGAPEYEFF (1939)')
    print('=' * 78)
    coordenadas = [decodificar_maraboli(b) for b in CIFRADO_ORIGINAL[:78]]
    ice = calcular_ice(coordenadas)
    print(f'Total coordenadas: {len(coordenadas)}')
    print(f'ICE: {ice:.2f}%')
    with open('resultados_decodificacion.json', 'w') as f:
        json.dump({'ice': ice, 'coords': coordenadas}, f)

if __name__ == '__main__':
    main()
