class EventoHistorial:
  """Registro de un evento del historial de vuelos."""
  def __init__(self, id: int, descripcion: str, fecha: str, hora: str):
    self.id = id
    self.descripcion = descripcion
    self.fecha = fecha
    self.hora = hora
