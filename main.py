from map_model import build_graph
from heuristics import heuristica_manziales
from search import a_estrella

grafo = build_graph()
ruta, costo = a_estrella(grafo, heuristica_manziales, 'Tunja', 'Manizales')

if ruta:
    print("Ruta optima encontrada:")
    print(" -> ".join(ruta))
    print(f"Distancia total: {costo} km")
else:
    print("No se encontró una ruta.")
