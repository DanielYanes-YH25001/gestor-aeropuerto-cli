from classes.GrafoRutas import GrafoRutas
import unittest

class TestGrafoRuta(unittest.TestCase):
    
    # Verifica que al agregar una arista, ambos aeropuertos se registren en el grafo
    def test_aeropuertos_en_grafo(self):
        grafo = GrafoRutas()
        grafo.agregar_arista("SAL", "JFK")
        
        self.assertIn("SAL", grafo.grafo)
        self.assertIn("JFK", grafo.grafo)
        
    # Verifica que las rutas devueltas son tuplas con origen y destino
    def test_formato_rutas(self):
        grafo = GrafoRutas()
        grafo.agregar_arista("SAL", "JFK")
        
        rutas = grafo.obtener_rutas()
        
        # Cada ruta debe ser una tupla con dos elementos (origen, destino)
        self.assertEqual(len(rutas[0]), 2)
        
    # Verifica que agregar varias aristas desde el mismo origen funcione bien
    def test_multiples_destinos(self):
        grafo = GrafoRutas()
        grafo.agregar_arista("SAL", "JFK")
        grafo.agregar_arista("SAL", "LAX")
        
        # El aeropuerto SAL debe tener dos destinos registrados
        self.assertEqual(len(grafo.grafo["SAL"]), 2)
        
if __name__ == "__main__":
    unittest.main()