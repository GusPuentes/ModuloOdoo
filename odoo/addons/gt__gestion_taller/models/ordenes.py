from odoo import models, fields

class Ordenes(models.Model):
    _name = 'gt__gestion_taller.ordenes'
    _description = 'Datos de las ordenes'

    def fecha_salida(self):
        if(self.terminado == True): 
            self.fecha_salida =  fields.Date.today

    def obtener_datos_piezas(self):
        for record in self:
            if record.piezas_id:
                pieza = self.env['gt__gestion_taller.piezas'].browse(record.piezas_id.id)
                # Accede a los datos del vehículo
                self.precio_pieza = pieza.precio_venta
                
    def obtener_datos_trabajador(self):            
        for record in self:
            if record.trabajadores_ids:
                trabajador = self.env['gt__gestion_taller.trabajadores'].browse(record.trabajadores_ids.id)
                self.precio_hora = trabajador.precio_hora

    def obtener_matricula(self):
        for record in self:
            if record.name:
                matricula = self.env['gt__gestion_taller.vehiculos'].browse(record.name.id)
                self.matricula = matricula.name

    def suma_total(self):
        self.total = self.precio_hora + self.precio_pieza

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
    precio_pieza = fields.Float(compute = 'obtener_datos_piezas', digits=(16, 2))
    precio_hora = fields.Float(compute = 'obtener_datos_trabajador', digits=(16, 2))
    total= fields.Float(compute = 'suma_total', digits=(16, 2))
    matricula = fields.Char(compute = 'obtener_matricula')