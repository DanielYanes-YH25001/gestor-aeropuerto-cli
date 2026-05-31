from classes.EventoHistorial import EventoHistorial
import unittest


class TestEventoHistorial(unittest.TestCase):
    
    # Prueba para verificar que los atributos del evento se asignan correctamente
    def test_atributos_correctos(self):
        evento = EventoHistorial(1, "Vuelo retrasado", "2024-06-01", "14:30")
        
        self.assertEqual(evento.id, 1)
        self.assertEqual(evento.descripcion, "Vuelo retrasado")
        self.assertEqual(evento.fecha, "2024-06-01")
        self.assertEqual(evento.hora, "14:30")
        
    # Prueba para verificar que dos eventos distintos tienen atributos diferentes
    def test_eventos_distintos(self):
        e1 = EventoHistorial(2, "Vuelo cancelado", "2024-06-02", "16:00")
        e2 = EventoHistorial(3, "Vuelo a tiempo", "2024-06-03", "18:00")
        
        self.assertNotEqual(e1.id, e2.id)
        self.assertNotEqual(e1.descripcion, e2.descripcion)
        self.assertNotEqual(e1.fecha, e2.fecha)
        self.assertNotEqual(e1.hora, e2.hora)
        
        
if __name__ == "__main__":
    unittest.main()