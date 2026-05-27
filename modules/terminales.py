from datos import nodo_aeropuerto
from classes.NodoAeropuerto import NodoAeropuerto


# Imprime las terminales del aeropuerto recursivamente
def recorrer_terminales(nodo_aeropuerto: NodoAeropuerto):
  if nodo_aeropuerto is None:
    return
  
  if nodo_aeropuerto.tipo == "aeropuerto":
    print(f"Aeropuerto: {nodo_aeropuerto.nombre}")
  else:
    print(f"Terminal: {nodo_aeropuerto.nombre}")

  for hijo in nodo_aeropuerto.hijos:
    recorrer_terminales(hijo)


# Menú para mostrar la información de las terminales
def menu_terminales():
  print("--- TERMINALES DEL AEROPUERTO ---")
  recorrer_terminales(nodo_aeropuerto)
