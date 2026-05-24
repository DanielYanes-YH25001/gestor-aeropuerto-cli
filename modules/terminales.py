from datos import nodo_aerouperto
from classes.NodoTerminal import NodoTerminal

# Imprime las terminales registradas del aeropuerto recursivamente
def recorrer_terminales(terminales: list[NodoTerminal]):
  if not terminales:
    return
  
  print(f"Terminal: {terminales[0].nombre}")
  recorrer_terminales(terminales[1:])

# Menú para mostrar la información de las terminales
def menu_terminales():
  print("--- TERMINALES DEL AEROPUERTO ---")
  print(f"Aeropuerto: {nodo_aerouperto.nombre}")

  terminales = nodo_aerouperto.hijos
  recorrer_terminales(terminales)
