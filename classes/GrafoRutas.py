class GrafoRutas:
  """Representa un grafo no dirigido de rutas de vuelo."""
  def __init__(self):
    self.grafo = {}

  def agregar_arista(self, origen: str, destino: str):
    """Agrega una conexión bidireccional entre dos aeropuertos."""
    if origen not in self.grafo:
      self.grafo[origen] = []

    if destino not in self.grafo:
      self.grafo[destino] = []

    self.grafo[origen].append(destino)
    self.grafo[destino].append(origen)

  def obtener_rutas(self):
    """Devuelve la lista de rutas únicas sin duplicar orígenes y destinos."""
    rutas = []
    vistas = set()

    for origen, destinos in self.grafo.items():
      for destino in destinos:
        par = (origen, destino)
        par_inverso = (destino, origen)

        if par_inverso in vistas:
          continue

        rutas.append(par)
        vistas.add(par)

    return rutas
