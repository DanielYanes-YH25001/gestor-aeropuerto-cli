from classes.NodoTerminal import NodoTerminal

class NodoAeropuerto:
  """Modelo de un aeropuerto con nodos terminales."""
  def __init__(self, nombre: str):
    self.nombre = nombre
    self.hijos = []

  def agregar_nodos(self, lista_nodos_terminales: list[NodoTerminal]):
    """Agrega terminales hijas al aeropuerto."""
    self.hijos.extend(lista_nodos_terminales)
