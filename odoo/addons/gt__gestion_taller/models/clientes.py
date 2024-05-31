from odoo import models, fields

class Clientes(models.Model):
    _name = 'gt__gestion_taller.clientes'
    _description = 'Datos de los clientes'

    name = fields.Char(String = "Nombre", required = True)
    apellido = fields.Char(String = "Apellidos", required=True)
    dni = fields.Many2one('gt__gestion_taller.vehiculos')
    telefono = fields.Integer(required=True)
    correo = fields.Char(required=True)
    direccion = fields.Char(String = "Direccion", required=True)