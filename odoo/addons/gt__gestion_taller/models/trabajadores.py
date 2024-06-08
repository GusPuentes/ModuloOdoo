from odoo import models, fields

class trabajadores(models.Model):
    _name = 'gt__gestion_taller.trabajadores'
    _description = 'Datos de los trabajadores'

    name = fields.Char(String = "Nombre", required = True)
    apellido = fields.Char(String = "Apellidos", required=True)
    puesto = fields.Char(String = 'Puesto')
    
    
    
    

