
    # EJERCICIO 6: Sobrecarga del método _str_
    def _str_(self):
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock}"

    # EJERCICIO 6: Sobrecarga del método _eq_ para comparar con ==
    def _eq_(self, otro_producto):
        # Primero validamos que el otro objeto sea de la misma clase
        if isinstance(otro_producto, ProductoKwikE):
            return (self.id_producto == otro_producto.id_producto) and (self.descripcion == otro_producto.descripcion)
        return False