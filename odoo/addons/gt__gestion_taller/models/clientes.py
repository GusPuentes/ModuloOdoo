from odoo import models, fields

class Clientes(models.Model):
    _name = 'gt__gestion_taller.clientes'
    _description = 'Datos de los clientes'

    name = fields.Char(String = "Nombre")
    apellido = fields.Char(String = "Apellidos")
    dni = fields.Char(String = "Dni")
    telefono = fields.Integer(String = "Telefono")
    correo = fields.Char()
    direccion = fields.Char(String = "Direccion")
    vehiculos_ids = fields.Many2many('gt__gestion_taller.vehiculos', String="vehiculos")