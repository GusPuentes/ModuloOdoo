from odoo import models, fields, api

class gt__gestio_taller(models.Model):
    _name = 'gt__gestio_taller.Clientes'
    _description = 'Datos de los clientes'

    name = fields.Char(String = "Nombre", required = True)
    apellido = fields.Char(String = "Apellidos", required=True)
    dni = fields.One2many('gt__gestio_taller.Vehículos')
    telefono = fields.Integer(required=True)
    correo = fields.Char(required=True)
    direccion = fields.Char(String = "Direccion", required=True)

