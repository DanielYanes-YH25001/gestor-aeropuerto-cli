from classes.Pasajero import Pasajero
import unittest

class TestPasajero(unittest.TestCase):
    
    # Prueba para verificar que los atributos del pasajero se asignan correctamente
    def test_atributos_correctos(self):
        pasajero = Pasajero(1, "Daniel Yanes", "AV123")
        
        self.assertEqual(pasajero.id, 1)
        self.assertEqual(pasajero.nombre, "Daniel Yanes")
        self.assertEqual(pasajero.n_vuelo, "AV123")
        
    # Prueba para verificar que dos pasajeros distintos tienen atributos diferentes
    def test_pasajeros_distintos(self):
        p1 = Pasajero(3, "Katherine Santos", "AV789")
        p2 = Pasajero(4, "Carlos Ayala", "AV101")
        
        self.assertNotEqual(p1.id, p2.id)
        self.assertNotEqual(p1.nombre, p2.nombre)
        self.assertNotEqual(p1.n_vuelo, p2.n_vuelo)
        
if __name__ == "__main__":
    unittest.main()