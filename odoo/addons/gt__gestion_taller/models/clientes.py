from odoo import models, fields

class Clientes(models.Model):
    _name = 'gt__gestion_taller.clientes'
    _description = 'Datos de los clientes'

    name = fields.Char(String = "Nombre", required = True)
    apellido = fields.Char(String = "Apellidos", required = True)
    dni = fields.Char(String = 'Dni', required = True)
    telefono = fields.Integer(string = "Telefono")
    correo = fields.Char()
    direccion = fields.Char(String = "Direccion")
    vehiculos_ids = fields.Many2many('gt__gestion_taller.vehiculos', string='vehiculos')