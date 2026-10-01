

from datetime  import date

class ProductoKwikE():
    def __init__(self, descripcion, id_producto,fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
    def cambiar_datos(self, descripcion= None, precio=None, stock = None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is None:
            self.stock = stock
    def expiracion(self):
        hoy = date.today()
        diferencia = self.fecha_vencimiento - hoy
        dias_restantes = diferencia.days
        if dias_restantes < 0:
            print(f"ALERTA: El producto '{self.descripcion}' ha expirado.")
            self.stock = 0
            
        return dias_restantes

