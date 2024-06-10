from odoo import models, fields, api

class trabajadores(models.Model):
    _name = 'gt__gestion_taller.trabajadores'
    _description = 'Datos de los trabajadores'

    @api.model
    def create(self, vals):
        # Crear el registro del empleado
        empleado = super(trabajadores, self).create(vals)
        
        # Crear el usuario asociado en res.users
        self.env['res.users'].create({
            'name': f"{empleado.name} {empleado.apellido}",
            'login': empleado.correo,  # El campo login es el nombre de usuario (correo electrónico)
            'email': empleado.correo,
            'password': empleado.apellido,  # Por ejemplo, usar el apellido como contraseña inicial (esto debería cambiarse a una contraseña segura)
        })
        
        return empleado

    name = fields.Char(String = "Nombre")
    apellido = fields.Char(String = "Apellidos")
    puesto = fields.Char(String = 'Puesto')
    precio_hora = fields.Float(String = 'Precio/Hora')
    correo = fields.Char('correo')
    
    
    
    

