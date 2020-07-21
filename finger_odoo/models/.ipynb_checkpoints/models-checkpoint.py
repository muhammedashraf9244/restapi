# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployees(models.Model):
    _inherit = 'hr.employee'
    device_id = fields.Char(string='Biometric Device ID')
    
    