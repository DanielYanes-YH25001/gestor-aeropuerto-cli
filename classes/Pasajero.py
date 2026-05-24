class Pasajero:
  """Modelo de pasajero con identificación y número de vuelo."""
  def __init__(self, id: int, nombre: str, n_vuelo: str):
    self.id = id
    self.nombre = nombre
    self.n_vuelo = n_vuelo
    