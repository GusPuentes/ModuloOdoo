from odoo import models, fields

class Piezas(models.Model):
    _name = 'gt__gestion_taller.piezas'
    _description = 'Datos de las piezas'

    def precio_venta(self):
        precio = (self.precio_compra * 0.12) + self.precio_compra
        self.precio_venta = (precio * 0.21) + precio

    name =fields.Char(String = "Nombre") 
    marca = fields.Char(String = "Marca")
    codigo = fields.Char(String = "Código de pieza")
    precio_compra = fields.Float('Precio de compra')
    precio_venta = fields.Float('Precio de venta', compute = precio_venta, readonly=True)
    stock = fields.Integer()
    
    
    

