class Nodo:
    def _init_(self, dato):
        self.dato = dato
        self.siguiente = None

class IteradorListaEnlazada:
    def _init_(self, cabeza):
        self.actual = cabeza
        
    def _iter_(self):
        return self
        
    def _next_(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual.dato
        self.actual = self.actual.siguiente
        return dato

class ListaEnlazada:
    def _init_(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def remover(self, dato_a_remover):
        actual = self.cabeza
        anterior = None
        while actual and actual.dato != dato_a_remover:
            anterior = actual
            actual = actual.siguiente
            
        if actual is None:
            return 
            
        if anterior is None:
            self.cabeza = actual.siguiente 
        else:
            anterior.siguiente = actual.siguiente

    def _iter_(self):
        return IteradorListaEnlazada(self.cabeza)