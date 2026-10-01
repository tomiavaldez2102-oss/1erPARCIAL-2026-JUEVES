from datetime import date, timedelta

class KwikEMart:
    def _init_(self):
        # Ejercicio 8.1: Atributos internos usando Listas Enlazadas
        self.pasillos = {
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada(),
            "Conveniencia": ListaEnlazada()
        }

    def agregar_producto(self, pasillo, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].agregar(producto)
        else:
            print(f"Error: El pasillo '{pasillo}' no existe.")

    def buscar_producto_por_id(self, id_producto):
        # Gracias al Iterador (Ej 8.2), podemos usar un bucle 'for' normal
        for nombre_pasillo, lista_enlazada in self.pasillos.items():
            for producto in lista_enlazada:
                if producto.id_producto == id_producto:
                    return producto, nombre_pasillo
        return None, None

    def actualizar_stock(self, id_producto, nuevo_stock):
        producto, _ = self.buscar_producto_por_id(id_producto)
        if producto:
            # Reutilizamos el método de la clase ProductoKwikE
            producto.cambiar_datos(stock=nuevo_stock) 
            print(f"Stock de {producto.descripcion} actualizado a {nuevo_stock}.")
        else:
            print("Producto no encontrado para actualizar.")

    def remover_producto(self, id_producto):
        producto, pasillo = self.buscar_producto_por_id(id_producto)
        if producto:
            self.pasillos[pasillo].remover(producto)
            print(f"Producto '{producto.descripcion}' removido del inventario.")

    def desechar_proximos_a_vencer(self):
        hoy = date.today()
        # Calculamos el umbral de 24 horas (1 día)
        limite_24h = hoy + timedelta(days=1) 
        
        # Guardamos las referencias primero para no romper la lista enlazada mientras la iteramos
        productos_a_desechar = []

        for nombre_pasillo, lista_enlazada in self.pasillos.items():
            for producto in lista_enlazada:
                if producto.fecha_vencimiento <= limite_24h:
                    productos_a_desechar.append((producto, nombre_pasillo))

        print("\n--- Apu está revisando las góndolas ---")
        for prod, pasillo in productos_a_desechar:
            print(f"Desechando: {prod.descripcion} (Vencimiento: {prod.fecha_vencimiento})")
            self.pasillos[pasillo].remover(prod)