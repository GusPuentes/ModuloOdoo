from odoo import models, fields

class Piezas(models.Model):
    _name = 'gt__gestion_taller.piezas'
    _description = 'Datos de las piezas'

    def precio_venta(self):
        precio = self.precio_compra * 0.12
        self.precio_venta = precio * 0.21

    nombre =fields.Char(String = "Nombre", required = True) 
    marca = fields.Char(String = "Marca", required = True)
    codigo = fields.Char(String = "Código de pieza", required = True)
    matricula = field_name_id = fields.Many2one('gt__gestion_taller.Clientes', string='matrícula')
    precio_compra = fields.Float('Precio de compra', required = True)
    precio_venta = fields.Float('Precio de compra', required = True, compute = precio_venta)
    stock = fields.Integer()
    
    
    

