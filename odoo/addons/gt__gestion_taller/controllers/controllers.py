# -*- coding: utf-8 -*-
# from odoo import http


# class GtGestionTaller(http.Controller):
#     @http.route('/gt__gestion_taller/gt__gestion_taller', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gt__gestion_taller/gt__gestion_taller/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gt__gestion_taller.listing', {
#             'root': '/gt__gestion_taller/gt__gestion_taller',
#             'objects': http.request.env['gt__gestion_taller.gt__gestion_taller'].search([]),
#         })

#     @http.route('/gt__gestion_taller/gt__gestion_taller/objects/<model("gt__gestion_taller.gt__gestion_taller"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gt__gestion_taller.object', {
#             'object': obj
#         })
