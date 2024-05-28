from odoo import models, fields

class Clientes(models.Model):
    _name = 'gt__gestion_taller.clientes'
    _description = 'Datos de los clientes'

    name = fields.Char(String = "Nombre", required = True)
    apellido = fields.Char(String = "Apellidos", required=True)
    dni = fields.Many2one('gt__gestion_taller.vehiculos', 'propietario_dni')
    telefono = fields.Integer(required=True)
    correo = fields.Char(required=True)
    direccion = fields.Char(String = "Direccion", required=True)
    # vehiculos_matriculas = fields.Many2One('gt__gestion_taller.Vehiculos', 'matricula', string='Matricula del vechiculo')