from datos import grafo

# Menú para presentar rutas de vuelo disponibles
def menu_rutas_vuelos():
  print("--- RUTAS DE VUELOS ---")
  rutas = grafo.obtener_rutas()

  if not rutas:
    print("No hay rutas disponibles en este momento.")
    return

  print("Se muestran 3 rutas de vuelo disponibles:")

  for indice, (origen, destino) in enumerate(rutas[:3], start = 1):
    print(f"{indice}. {origen} -> {destino}")
