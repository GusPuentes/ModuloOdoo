# -*- coding: utf-8 -*-
# from odoo import http


# class GtGestioTaller(http.Controller):
#     @http.route('/gt__gestio_taller/gt__gestio_taller', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gt__gestio_taller/gt__gestio_taller/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gt__gestio_taller.listing', {
#             'root': '/gt__gestio_taller/gt__gestio_taller',
#             'objects': http.request.env['gt__gestio_taller.gt__gestio_taller'].search([]),
#         })

#     @http.route('/gt__gestio_taller/gt__gestio_taller/objects/<model("gt__gestio_taller.gt__gestio_taller"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gt__gestio_taller.object', {
#             'object': obj
#         })
