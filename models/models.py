# -*- coding: utf-8 -*-

from odoo import models, fields, api


class joinet_test(models.Model):
    _name = 'joinet_test.joinet_test'
    _description = 'joinet_test.joinet_test'
    _rec_name = 'nombre'

    nombre = fields.Char("Nombre")
    marca = fields.Char("Marca")
    modelo = fields.Char("Modelo")
    direccion_mac = fields.Char("Mac")
    direccion_anydesk = fields.Char("Any desk")
    password_anydesk = fields.Char("any desk psw")
    licencia_mcf = fields.Char("Licencia Mcafee")
    licencia_mbp = fields.Char("Licencia MBPOS")
    tarjeta_grafica = fields.Char(string="Tarjeta gráfica")
    otro_hardware = fields.Text(string="Otro software")
    observaciones = fields.Text(string="Observaciones")
