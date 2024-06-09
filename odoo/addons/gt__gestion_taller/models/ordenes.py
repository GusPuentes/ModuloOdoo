from odoo import models, fields

class Ordenes(models.Model):
    _name = 'gt__gestion_taller.ordenes'
    _description = 'Datos de las ordenes'

    def fecha_salida(self):
        if(self.terminado == True): 
            self.fecha_salida =  fields.Date.today

        
    marca = fields.Char(String = "Marca")
    modelo = fields.Char(String = "Modelo")
    name = fields.Many2one('gt__gestion_taller.vehiculos', string='matricula')
    fecha_entrada = fields.Date('Fecha de entrada')
    piezas_id = fields.Many2one('gt__gestion_taller.piezas')
    trabajadores_ids = fields.Many2many('gt__gestion_taller.trabajadores', string='Trabajadores Asignados')
    fallos = fields.Char(String = "Descripcion de los fallos")
    diagnostico = fields.Char(String = "Diagnostico mecánico")
    fecha_salida = fields.Date('Fecha de salida')
    terminado = fields.Boolean(String = 'Terminado', default = False)
