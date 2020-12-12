# -*- coding: utf-8 -*-
# from odoo import http


# class JoinetTest(http.Controller):
#     @http.route('/joinet_test/joinet_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/joinet_test/joinet_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('joinet_test.listing', {
#             'root': '/joinet_test/joinet_test',
#             'objects': http.request.env['joinet_test.joinet_test'].search([]),
#         })

#     @http.route('/joinet_test/joinet_test/objects/<model("joinet_test.joinet_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('joinet_test.object', {
#             'object': obj
#         })
