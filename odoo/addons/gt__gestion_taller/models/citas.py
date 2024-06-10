from odoo import models, fields, api

class citas(models.Model):
    _name = 'gt__gestion_taller.citas'
    _description = 'Calendario de citas'

    name = fields.Char(String ='Matrícula' )
    marca = fields.Char(String = "Vehiculo")
    telefono = fields.Char(String = "Teléfono")
    entrada = fields.Datetime('Entrada')
    salida = fields.Datetime('salida')