from modules import pasajeros, historial_vuelos, asientos_pasajeros, terminales, rutas_vuelos


# Función principal que muestra el menú y redirige a cada sección
def main():
  while True:
    # Menú principal
    print("\n=========================")
    print("  GESTOR DE AEROPUERTO")
    print("=========================")
    print("1. Gestionar Pasajeros")
    print("2. Gestionar Historial de Vuelos")
    print("3. Mostrar Asientos de Vuelo")
    print("4. Mostrar Terminales de Aeropuerto")
    print("5. Mostrar Rutas de Vuelo")
    print("6. Salir del gestor")

    # Solicitamos al usuario que seleccione una opción
    opcion = input("Seleccione una sección: ")

    # Validamos la opción ingresada por el usuario
    if opcion == "1":
      pasajeros.menu_pasajeros()

    elif opcion == "2":
      historial_vuelos.menu_historial_vuelos()

    elif opcion == "3":
      asientos_pasajeros.menu_asientos_pasajeros()

    elif opcion == "4":
      terminales.menu_terminales()

    elif opcion == "5":
      rutas_vuelos.menu_rutas_vuelos()

    elif opcion == "6":
      print("Saliendo del gestor de aeropuerto...")
      break

    else:
      print("Opción inválida. Por favor, seleccione de las opciones.")


# Punto de entrada del programa; evita que la función principal
# se ejecute si este archivo no se ejecuta directamente
if __name__ == "__main__":
  main()
