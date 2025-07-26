import heapq

def a_estrella(graph, heuristica, inicio, objetivo):
    frontera = [(heuristica[inicio], 0, inicio, [inicio])]
    visitados = set()

    while frontera:
        f, costo_actual, nodo_actual, camino = heapq.heappop(frontera)

        if nodo_actual == objetivo:
            return camino, costo_actual

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        for vecino, costo in graph.edges.get(nodo_actual, []):
            if vecino not in visitados:
                nuevo_costo = costo_actual + costo
                heur = heuristica.get(vecino, float('inf'))
                heapq.heappush(frontera, (nuevo_costo + heur, nuevo_costo, vecino, camino + [vecino]))

    return None, float('inf')
