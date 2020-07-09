# -*- coding: utf-8 -*-
from odoo import http

class Restapi(http.Controller):
     @http.route('/restapi/restapi/', auth='public')
     def index(self, **kw):
         return "Hello, world"
    
     @http.route('/web/session/getauthentication',type='json',auth='none')
     def getauthentication(self,db,username,password,base_location=None):
         request.session.getauthentication(db,username,password)
         return "Muhammed Ashraf"

#     @http.route('/restapi/restapi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('restapi.listing', {
#             'root': '/restapi/restapi',
#             'objects': http.request.env['restapi.restapi'].search([]),
#         })

#     @http.route('/restapi/restapi/objects/<model("restapi.restapi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restapi.object', {
#             'object': obj
#         })
