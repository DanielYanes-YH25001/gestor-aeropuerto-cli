from classes.NodoAsiento import NodoAsiento
import unittest
from classes.Pasajero import Pasajero

class TestNodoAsiento(unittest.TestCase):
    
    # Verifica que al crear un nodo, next empieza en None
    def test_next_defecto(self):
        nodo = NodoAsiento(1, None)
        
        self.assertIsNone(nodo.next)
        
    # Verifica que el numero de asiento se asigna correctamente
    def test_numero_asiento(self):
        pasajero = Pasajero(1, "Daniel Yanes", "AV123")
        nodo = NodoAsiento(1, pasajero)
        
        self.assertEqual(nodo.n_asiento, 1)
        
    # Verifica que el pasajero guardado en el nodo es el correcto
    def test_pasajero_correcto(self):
        pasajero = Pasajero(1, "Katherine Santos", "AV456")
        nodo = NodoAsiento(1, pasajero)
        
        self.assertEqual(nodo.pasajero.nombre, "Katherine Santos")
        self.assertEqual(nodo.pasajero.id, 1)
        self.assertEqual(nodo.n_asiento, 1)
        
    # Verifica que se pueden enlazar dos nodos correctamente
    def test_enlazar_nodos(self):
        pasajero1 = Pasajero(1, "Daniel Yanes", "AV123")
        pasajero2 = Pasajero(2, "Katherine Santos", "AV456")
        
        nodo1 = NodoAsiento(1, pasajero1)
        nodo2 = NodoAsiento(2, pasajero2)
        
        # Se enlazan los nodos
        nodo1.next = nodo2
        
        self.assertIsNotNone(nodo1.next)
        self.assertEqual(nodo1.next.n_asiento, 2)
        self.assertEqual(nodo1.next.pasajero.nombre, "Katherine Santos")
        
    # Enlazar tres nodos en cadena
    def test_cadena_nodos(self):
        pasajero1 = Pasajero(1, "Carlos Ayala", "AV789")
        pasajero2 = Pasajero(2, "Daniel Yanes", "AV123")
        pasajero3 = Pasajero(3, "Katherine Santos", "AV456")
        
        nodo1 = NodoAsiento(1, pasajero1)
        nodo2 = NodoAsiento(2, pasajero2)
        nodo3 = NodoAsiento(3, pasajero3)
        
        # Se enlazan los nodos en cadena
        nodo1.next = nodo2
        nodo2.next = nodo3
        
        # Desde nodo1 se recorre hasta nodo3
        self.assertEqual(nodo1.next.next.pasajero.nombre, "Katherine Santos")
        
if __name__ == '__main__':
    unittest.main()