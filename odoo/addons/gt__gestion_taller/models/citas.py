from odoo import models, fields, api

class Vehiculos(models.Model):
    _name = 'gt__gestion_taller.vehiculos'
    _description = 'Datos de los vehiculos'

    name = fields.Char(String ='Matrícula' )
    marca = fields.Char(String = "Vehiculo")
    telefono = fields.Char(String = "Teléfono")
    
    