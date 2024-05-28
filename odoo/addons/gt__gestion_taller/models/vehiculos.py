from odoo import models, fields

class Vehiculos(models.Model):
    _name = 'gt__gestion_taller.vehiculos'
    _description = 'Datos de los vehiculos'

    marca = fields.Char(String = "Nombre", required = True)
    modelo = fields.Char(String = "Apellidos", required=True)
    propietario_dni = fields.One2many('gt__gestion_taller.Clientes','dni')
    # matricula = fields.One2Many('gt_gestion_taller.ordenes', 'vehiculos_matriculas')
    
    
    

