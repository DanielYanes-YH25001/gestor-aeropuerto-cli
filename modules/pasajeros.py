import datos
from classes.Pasajero import Pasajero
from utils import validar_entrada

# Menú para visualizar y registrar pasajeros
def menu_pasajeros():
  while True:
    print("\n--- SECCIÓN: GESTIÓN DE PASAJEROS ---")
    print("1. Ver lista de pasajeros")
    print("2. Agregar nuevo pasajero")
    print("3. Volver al menú principal")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
      print("\n--- LISTA DE PASAJEROS ---")
      
      if not datos.pasajeros:
        print("No hay pasajeros en espera.")
      else:
        for pasajero in datos.pasajeros:
          print(f"ID: {pasajero.id} | Nombre: {pasajero.nombre} | N° Vuelo: {pasajero.n_vuelo}")
    
    elif opcion == "2":
      nombre = validar_entrada("Ingrese el nombre del pasajero: ")
      n_vuelo = validar_entrada("Ingrese el número de vuelo: ")

      nuevo_pasajero = Pasajero(
        id = datos.id_pasajero_actual,
        nombre = nombre,
        n_vuelo = n_vuelo
      )

      datos.pasajeros.append(nuevo_pasajero)
      print(f"Éxito: Pasajero '{nombre}' creado con ID {datos.id_pasajero_actual}.")
      datos.id_pasajero_actual += 1
    
    elif opcion == "3":
      break
    
    else:
      print("Opción inválida. Por favor, seleccione una de las tres opciones.")
