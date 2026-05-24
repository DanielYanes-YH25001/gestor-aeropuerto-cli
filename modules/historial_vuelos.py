import datos
from classes.EventoHistorial import EventoHistorial
from utils import validar_entrada
from datetime import datetime

# Devuelve la fecha y la hora actual en un formato legible
def obtener_fecha_hora_actual():
  now = datetime.now()
  fecha = f"{now.day}/{now.month}/{now.year}"
  hora = f"{now.hour}:{now.minute}:{now.second}"

  return {
    "fecha": fecha,
    "hora": hora
  }

# Menú para consultar o agregar eventos al historial de vuelos
def menu_historial_vuelos():
  while True:
    print("\n--- SECCIÓN: GESTIÓN DE HISTORIAL DE VUELOS ---")
    print("1. Ver historial de vuelos")
    print("2. Agregar nuevo evento al historial")
    print("3. Volver al menú principal")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
      print("\n--- HISTORIAL DE VUELOS ---")
      
      if not datos.historial_vuelos:
        print("Historial vacío.")
      else:
        for evento in datos.historial_vuelos:
          print(f"ID: {evento.id} | Descripción: {evento.descripcion} | Fecha: {evento.fecha} | Hora: {evento.hora}")
    
    elif opcion == "2":
      descripcion_evento = validar_entrada("Ingrese la descripción del evento: ")
      fecha_hora = obtener_fecha_hora_actual()

      nuevo_evento = EventoHistorial(
        id = datos.id_evento_historial_actual,
        descripcion = descripcion_evento,
        fecha = fecha_hora["fecha"],
        hora = fecha_hora["hora"]
      )

      datos.historial_vuelos.appendleft(nuevo_evento)
      print(f"Éxito: Evento creado con ID {datos.id_evento_historial_actual}.")
      datos.id_evento_historial_actual += 1
    
    elif opcion == "3":
      break
    
    else:
      print("Opción inválida. Por favor, seleccione una de las opciones.")
