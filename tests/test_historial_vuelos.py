from modules.historial_vuelos import obtener_fecha_hora_actual
from unittest.mock import patch, Mock
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
        
    # Verifica que la fecha y hora se obtienen correctamente usando mock
    @patch("modules.historial_vuelos.datetime")
    def test_obtener_fecha_hora_actual(self, mock_datetime):
        mock_fecha_hora = Mock()
        mock_fecha_hora.day = 30
        mock_fecha_hora.month = 5
        mock_fecha_hora.year = 2026
        mock_fecha_hora.hour = 15
        mock_fecha_hora.minute = 30
        mock_fecha_hora.second = 25

        mock_datetime.now.return_value = mock_fecha_hora

        resultado = obtener_fecha_hora_actual()

        self.assertEqual(resultado, {
            "fecha": "30/5/2026",
            "hora": "15:30:25"
        })
        
        
if __name__ == '__main__':
    unittest.main()