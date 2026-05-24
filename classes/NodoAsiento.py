from classes.Pasajero import Pasajero

class NodoAsiento:
  """Nodo para una lista enlazada de asientos y pasajeros."""
  def __init__(self, n_asiento: str = None, pasajero: Pasajero = None):
    self.n_asiento = n_asiento
    self.pasajero = pasajero
    self.next = None
