from odoo import models, fields, api

class Vehiculos(models.Model):
    _name = 'gt__gestion_taller.vehiculos'
    _description = 'Datos de los vehiculos'

    name = fields.Char(String ='Matrícula' )
    marca = fields.Char(String = "Nombre")
    modelo = fields.Char(String = "Apellidos")
    orden_ids = fields.One2many('gt__gestion_taller.ordenes', 'name', string='Órdenes')
    