from modules.historial_vuelos import obtener_fecha_hora_actual
import unittest

class TestObtenerFechaHoraActual(unittest.TestCase):
    
    # Verifica que el metodo devuelve un diccionario
    def test_devuelve_diccionario(self):
        resultado = obtener_fecha_hora_actual()
        
        self.assertIsInstance(resultado, dict)
        
    # Verifica que el diccionario contiene las claves "fecha" y "hora"
    def test_claves_diccionario(self):
        resultado = obtener_fecha_hora_actual()
        
        self.assertTrue(resultado["fecha"])
        self.assertTrue(resultado["hora"])
        
if __name__ == '__main__':
    unittest.main()