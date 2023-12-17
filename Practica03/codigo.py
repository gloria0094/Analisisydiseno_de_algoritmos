
import random
import heapq
import time 

iniciotiem=time.time()

class Graph:
    def __init__(self):
        self.graph = {}

    def agregar_vertice(self, vertice):
        self.graph[vertice] = {}

    def agregar_arista(self, inicio, fin, peso):
        self.graph[inicio][fin] = peso
        self.graph[fin][inicio] = peso

    def dijkstra(self, inicio):
        distancias = {vertice: float('infinity') for vertice in self.graph}
        distancias[inicio] = 0

        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            distancia_actual, vertice_actual = heapq.heappop(cola_prioridad)

            if distancia_actual > distancias[vertice_actual]:
                continue

            for vecino, peso in self.graph[vertice_actual].items():
                distancia_total = distancias[vertice_actual] + peso

                if distancia_total < distancias[vecino]:
                    distancias[vecino] = distancia_total
                    heapq.heappush(cola_prioridad, (distancia_total, vecino))

        return distancias

# Crear un grafo de ejemplo
grafo = Graph()
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')
grafo.agregar_vertice('G')




grafo.agregar_arista('A', 'B', 19)
grafo.agregar_arista('A', 'E', 38)
grafo.agregar_arista('A', 'F', 12)
grafo.agregar_arista('A', 'D', 44)
grafo.agregar_arista('B', 'C', 26)
grafo.agregar_arista('B', 'D', 24)
grafo.agregar_arista('C', 'D', 14)
grafo.agregar_arista('C', 'F', 7)
grafo.agregar_arista('C', 'G', 10)
grafo.agregar_arista('D', 'F', 3)
grafo.agregar_arista('F', 'E', 9)
grafo.agregar_arista('F', 'G', 16)
grafo.agregar_arista('G', 'E', 23)

inicio_dijkstra = 'A'
resultados_dijkstra = grafo.dijkstra(inicio_dijkstra)
fintiem=time.time()
# Imprimir los resultados
for vertice, distancia in resultados_dijkstra.items():
    print(f"Distancia mínima desde {inicio_dijkstra} hasta {vertice}: {distancia}")

fintiem=time.time()
total_tiempo=fintiem-iniciotiem

print(f"El tiempo es: {total_tiempo}")

