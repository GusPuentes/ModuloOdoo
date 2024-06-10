from odoo import models, fields, api

class Ordenes(models.Model):
    _name = 'gt__gestion_taller.ordenes'
    _description = 'Datos de las ordenes'

    def fecha_salida(self):
        if(self.terminado == True): 
            self.fecha_salida =  fields.Date.today

    def obtener_datos_piezas(self):
        if self.diagnosticado == True:
            for record in self:
                if record.piezas_id:
                    pieza = self.env['gt__gestion_taller.piezas'].browse(record.piezas_id.id)
                    # Accede a los datos del vehículo
                    self.precio_pieza = pieza.precio_venta
        else:
            self.precio_pieza = 0

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
    
    def obtener_correo(self):            
        for record in self:
            if record.cliente_id:
                cliente = self.env['gt__gestion_taller.clientes'].browse(record.cliente_id.id)
                self.correo = cliente.correo
    
    def send_mail_template(self):
        template = self.en.ref('send_email.example_email_template')
        self.env['mail.template'].browase(template.id).send_mail(self.id)

    def enviar_correo_directo(self):
        for record in self:
            
            email_to = self.correo
            subject = "Presupuesto de Orden"
            body_html = """
                <p>Estimado/a </p>
                <p>Adjunto encontrará el presupuesto de su orden.</p>
                <p>Atentamente,</p>
                <p>Su Taller</p>
            """.format(record.cliente_id.name)

            mail_values = {
                'subject': subject,
                'body_html': body_html,
                'email_from': self.env.user.email,
                'email_to': email_to,
                'auto_delete': False,  # No eliminar el correo después de enviarlo
            }

            if record.attachment_ids:
                attachments = [(4, attachment.id) for attachment in record.attachment_ids]
                mail_values['attachment_ids'] = attachments


            mail = self.env['mail.mail'].create(mail_values)
            mail.send()

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
    diagnosticado = fields.Boolean('diagnosticado', default = False)
    cliente_id = fields.Many2one('gt__gestion_taller.clientes', string='cliente')
    correo = fields.Char('correo',compute = 'obtener_correo')
    attachment_ids = fields.Many2many('ir.attachment', string="Adjuntos")
