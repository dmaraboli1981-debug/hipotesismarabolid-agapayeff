# -*- coding: utf-8 -*-
# SCRIPT 02: SIMULACION MONTE CARLO
# Autor: Diego Hector Maraboli | Fecha: 2026-04-15

import numpy as np
import json

N_SIMULACIONES = 1000
ICE_OBSERVADO = 51.3

def calcular_ice(coords):
    return sum(1 for lat, lon in coords if 
        (70 <= abs(lat) <= 85 and 60 <= lon <= 95) or
        (25 <= abs(lat) <= 30 and 47 <= lon <= 55)) / len(coords) * 100

def main():
    np.random.seed(42)
    ice_sim = [calcular_ice([(np.random.uniform(-90,90), np.random.uniform(0,180)) 
              for _ in range(78)]) for _ in range(N_SIMULACIONES)]
    ice_max = max(ice_sim)
    print(f'ICE Observado: {ICE_OBSERVADO}%')
    print(f'ICE Max Simulado: {ice_max:.2f}%')
    print(f'p-valor: {"< 0.001 ***" if ICE_OBSERVADO > ice_max else "NS"}')
    with open('resultados_monte_carlo.json', 'w') as f:
        json.dump({'ice_max': ice_max}, f)

if __name__ == '__main__':
    main()
