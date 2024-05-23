# -*- coding: utf-8 -*-
# from odoo import http


# class GtGestion.taller(http.Controller):
#     @http.route('/gt__gestion.taller/gt__gestion.taller', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gt__gestion.taller/gt__gestion.taller/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gt__gestion.taller.listing', {
#             'root': '/gt__gestion.taller/gt__gestion.taller',
#             'objects': http.request.env['gt__gestion.taller.gt__gestion.taller'].search([]),
#         })

#     @http.route('/gt__gestion.taller/gt__gestion.taller/objects/<model("gt__gestion.taller.gt__gestion.taller"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gt__gestion.taller.object', {
#             'object': obj
#         })
