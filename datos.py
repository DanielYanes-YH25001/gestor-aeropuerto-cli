from collections import deque
from classes.NodoAeropuerto import NodoAeropuerto
from classes.NodoTerminal import NodoTerminal
from classes.GrafoRutas import GrafoRutas

# Listas globales para almacenar los datos del aeropuerto
pasajeros = deque()
historial_vuelos = deque()
lista_asientos = []

# Contadores de IDs automáticos para nuevos registros
id_pasajero_actual = 1
id_evento_historial_actual = 1
id_asiento_actual = 1

# Inicialización del nodo aeropuerto y sus nodos terminales
nodo_aerouperto = NodoAeropuerto("Aeropuerto Internacional San Óscar Arnulfo Romero y Galdámez")
nodo_terminal1 = NodoTerminal("Pasajeros")
nodo_terminal2 = NodoTerminal("Carga")
nodo_aerouperto.agregar_nodos([nodo_terminal1, nodo_terminal2])

# Grafo que guarda las rutas disponibles para un vuelo en particular
grafo = GrafoRutas()

grafo.agregar_arista(
  "Aeropuerto Internacional de El Salvador (SAL)",
  "Aeropuerto John F. Kennedy, Nueva York (JFK), Estados Unidos"
)

grafo.agregar_arista(
  "Aeropuerto Internacional de El Salvador (SAL)",
  "Aeropuerto Internacional Arturo Merino Benítez, Santiago de Chile (SCL), Chile"
)

grafo.agregar_arista(
  "Aeropuerto Internacional de El Salvador (SAL)",
  "Aeropuerto Internacional de Tocumen, Ciudad de Panamá (PTY), Panamá"
)
