class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, cost):
        self.edges.setdefault(from_node, []).append((to_node, cost))
        self.edges.setdefault(to_node, []).append((from_node, cost))  # Grafo no dirigido

def build_graph():
    g = Graph()
    g.add_edge('Tunja', 'Villa de Leyva', 35)
    g.add_edge('Villa de Leyva', 'Chiquinquira', 34)
    g.add_edge('Tunja', 'Tocancipa', 105)
    g.add_edge('Tocancipa', 'Bogota', 40)
    g.add_edge('Chiquinquirá', 'Zipaquira', 90)
    g.add_edge('Zipaquira', 'Chia', 25)
    g.add_edge('Chia', 'Bogota', 16)
    g.add_edge('Bogota', 'Soacha', 26)
    g.add_edge('Soacha', 'Giradot', 45)
    g.add_edge('Soacha', 'Fusagasuga', 30)
    g.add_edge('Fusagasuga', 'Melgar', 34)
    g.add_edge('Melgar', 'Ibague', 70)
    g.add_edge('Ibague', 'Armenia', 47)
    g.add_edge('Armenia', 'Pereira', 39)
    g.add_edge('Pereira', 'Manizales', 46)
    g.add_edge('La Vega', 'Guaduas', 40)
    g.add_edge('Bogota', 'Villeta', 66)
    g.add_edge('Villeta', 'Manizales', 115)
    return g
