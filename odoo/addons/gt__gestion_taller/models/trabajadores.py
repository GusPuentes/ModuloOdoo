from odoo import models, fields

class trabajadores(models.Model):
    _name = 'gt__gestion_taller.trabajadores'
    _description = 'Datos de los trabajadores'

    name = fields.Char(String = "Nombre")
    apellido = fields.Char(String = "Apellidos")
    puesto = fields.Char(String = 'Puesto')
    precio_hora = fields.Float(String = 'Precio/Hora')
    
    
    
    

