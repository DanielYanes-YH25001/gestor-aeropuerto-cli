from classes.NodoAeropuerto import NodoAeropuerto
import unittest

class TestNodoAeropuerto(unittest.TestCase):
    
    # Verifica que el tipo por defecto de unu nodo es "aeropuerto"
    def test_tipo_defecto(self):
        nodo = NodoAeropuerto("Aeropuerto Internacional")
        
        self.assertEqual(nodo.tipo, "aeropuerto")
        
    # Verifica que el nombre se asigna correctamente
    def test_nombre_correcto(self):
        nodo = NodoAeropuerto("Aeropuerto Internacional San Oscar Arnulfo Romero")
        
        self.assertEqual(nodo.nombre, "Aeropuerto Internacional San Oscar Arnulfo Romero")
        
    # Verifica que n nodo recien creado no tiene hijos
    def test_sin_hijos(self):
        nodo = NodoAeropuerto("Aeropuerto Internacional San Oscar Arnulfo Romero")
        
        self.assertEqual(len(nodo.hijos), 0)
        
    # Verifica que agregar terminales aumenta correctamente la lista de hijos
    def test_agregar_terminales(self):
        aeropuerto = NodoAeropuerto("Aeropuerto Internacional San Oscar Arnulfo Romero")
        terminal1 = NodoAeropuerto("Terminal pasajeros", "terminal")
        terminal2 = NodoAeropuerto("Terminal carga", "terminal")
        
        aeropuerto.agregar_nodos([terminal1, terminal2])
        
        # Deben haber 2 hijos en el aeropuerto
        self.assertEqual(len(aeropuerto.hijos), 2)
        
    # Verifica que agregar una lista vacia no rompe nada
    def test_lista_vacia(self):
        aeropuerto = NodoAeropuerto("Aeropuerto Internacional San Oscar Arnulfo Romero")
        
        aeropuerto.agregar_nodos([])
        
        self.assertEqual(len(aeropuerto.hijos), 0)
        
    # Verifica que el tipo "terminal" se asigna correctamente
    def test_tipo_terminal(self):
        terminal = NodoAeropuerto("Terminal pasajeros", "terminal")
        
        self.assertEqual(terminal.tipo, "terminal") 
        
if __name__ == '__main__':
    unittest.main()