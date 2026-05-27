import datos
from classes.NodoAsiento import NodoAsiento


# Recorre la lista enlazada de asientos e imprime sus datos
def recorrer_asientos(nodo_inicial: NodoAsiento):
  print("--- ASIENTOS DE VUELO ---")
  while nodo_inicial.next:
    pasajero = nodo_inicial.pasajero
    print(f"N° Asiento: {nodo_inicial.n_asiento} | Nombre: {pasajero.nombre} | N° Vuelo {pasajero.n_vuelo}")
    nodo_inicial = nodo_inicial.next


# Menú que crea la lista de asientos enlazados para los pasajeros
def menu_asientos_pasajeros():
  datos.lista_asientos = []
  datos.id_asiento_actual = 1

  asiento_nulo = NodoAsiento()

  for pasajero in datos.pasajeros:
    asiento = NodoAsiento(datos.id_asiento_actual, pasajero)
    datos.lista_asientos.append(asiento)
    datos.id_asiento_actual += 1

  for i in range(len(datos.lista_asientos)):
    asiento = datos.lista_asientos[i]
    try:
      asiento.next = datos.lista_asientos[i + 1]
    except IndexError:
      asiento.next = asiento_nulo

  try:
    recorrer_asientos(datos.lista_asientos[0])
  except IndexError:
    print("Error: No hay pasajeros en vuelo.")
