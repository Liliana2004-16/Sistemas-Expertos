from map_model import build_graph
from heuristics import heuristica_manziales
from search import a_estrella
from models.predictor import TiempoViajePredictor


print(" Ruta mas corta de Tunja a Manizales (con algoritmo A*)")
grafo = build_graph()
ruta, costo = a_estrella(grafo, heuristica_manziales, 'Tunja', 'Manizales')

if ruta:
    print("Ruta encontrada: " + " -> ".join(ruta))
    print(f"Distancia total estimada: {costo} km")
else:
    print("No se encontró una ruta.")

print("Entrenando modelo de prediccion supervisada con datos historicos...")
predictor = TiempoViajePredictor()
predictor.entrenar("data/dataset_rutas_contraflujo.csv")  

nueva_muestra = {
    'Origen': 'Tunja',
    'Destino': 'Manizales',
    'Distancia': 400,
    'Hora': 10,
    'Dia': 'Martes',
    'Clima': 'Soleado',
    'Evento': 'Obra'
}
tiempo_estimado = predictor.predecir(nueva_muestra)

print("Prediccion del tiempo real de viaje:")
print(f"Condiciones: {nueva_muestra}")
print(f"Tiempo estimado de viaje: {tiempo_estimado:.2f} horas")
