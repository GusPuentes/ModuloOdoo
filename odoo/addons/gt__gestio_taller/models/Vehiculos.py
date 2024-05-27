from odoo import models, fields

class gt__gestio_taller(models.Model):
    _name = 'gt__gestio_taller.Vehiculos'
    _description = 'Datos de los vehiculos'

    marca = fields.Char(String = "Nombre", required = True)
    modelo = fields.Char(String = "Apellidos", required=True)
    matricula = fields.Many2one('gt__gestio_taller.Clientes', string='matrícula')
    
    
    

