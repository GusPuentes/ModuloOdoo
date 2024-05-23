# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gt__gestion.taller(models.Model):
#     _name = 'gt__gestion.taller.gt__gestion.taller'
#     _description = 'gt__gestion.taller.gt__gestion.taller'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
