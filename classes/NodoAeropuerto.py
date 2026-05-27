from __future__ import annotations


class NodoAeropuerto:
  """Modelo de un aeropuerto con nodos terminales."""
  def __init__(self, nombre: str, tipo: str = "aeropuerto"):
    self.nombre = nombre
    self.tipo = tipo
    self.hijos = []

  def agregar_nodos(self, lista_nodos_terminales: list[NodoAeropuerto]):
    """Agrega terminales hijas al aeropuerto."""
    self.hijos.extend(lista_nodos_terminales)
