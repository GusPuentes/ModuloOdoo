from odoo import models, fields

class Ordenes(models.Model):
    _name = 'gt__gestion_taller.ordenes'
    _description = 'Datos de las ordenes'

    def cod_order(self):
        precio = self.precio_compra * 0.12
        self.precio_venta = precio * 0.21

    marca = fields.Char(String = "Marca", required = True)
    modelo = fields.Char(String = "Modelo", required=True)
    # matricula_vehiculo = fields.Many2one('gt__gestion_taller.Clientes')
    fecha_entrada = fields.Date('Fecha de entrada')
    piezas = fields.Json(string = "información adicional", default ={}) 
    
    

