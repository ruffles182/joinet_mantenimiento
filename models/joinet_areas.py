# -*- coding: utf-8 -*-

from odoo import models, fields, api

class joinet_areas(models.Model):
    _name = 'joinet_test.joinet_areas'
    _description = 'joinet_test.joinet_areas'
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre Area")

class joinet_asignacion(models.Model):
    _name = 'joinet_test.joinet_asignacion'
    _description = 'joinet_test.joinet_asignacion'

    pc = fields.Many2one('joinet_test.joinet_test','Pc')
    area = fields.Many2one('joinet_test.joinet_areas', 'Area')
    ip = fields.Char('ip')
    