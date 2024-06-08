from odoo import models, fields, api

class Vehiculos(models.Model):
    _name = 'gt__gestion_taller.vehiculos'
    _description = 'Datos de los vehiculos'

    name = fields.Char(String ='Matrícula', required =True )
    marca = fields.Char(String = "Nombre", required = True)
    modelo = fields.Char(String = "Apellidos", required=True)
    orden_ids = fields.One2many('gt__gestion_taller.ordenes', 'name', string='Órdenes')
    

    
    
    

