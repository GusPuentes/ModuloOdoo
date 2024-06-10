from odoo import models, fields,api

class Clientes(models.Model):
    _name = 'gt__gestion_taller.clientes'
    _description = 'Datos de los clientes'

    @api.model
    def create(self, vals):
        # Crear el registro del cliente
        cliente = super(Clientes, self).create(vals)
        
        # Crear el contacto asociado en res.partner
        self.env['res.partner'].create(
        {
            'name': f"{cliente.name} {cliente.apellido}",
            'email': cliente.correo,
            'phone': cliente.telefono,
            'street':cliente.direccion,
            'ref':cliente.dni,
            'customer_rank': 1,
        })
        
        return cliente

    name = fields.Char(String = "Nombre")
    apellido = fields.Char(String = "Apellidos")
    dni = fields.Char(String = "Dni")
    telefono = fields.Char(String = "Telefono")
    correo = fields.Char()
    direccion = fields.Char(String = "Direccion")
    vehiculos_ids = fields.Many2many('gt__gestion_taller.vehiculos', String="vehiculos")
    customer_rank = fields.Binary('customer_rank')

    