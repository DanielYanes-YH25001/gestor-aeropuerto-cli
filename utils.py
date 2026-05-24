def validar_entrada(mensaje: str):
  """Solicita al usuario un valor no vacío y lo devuelve."""
  
  while True:
    valor = input(mensaje).strip()
    if valor:
      return valor
    else:
      print("Error: El campo no puede estar vacío. Intente de nuevo.")
