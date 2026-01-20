# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    json_pe_api_token = fields.Char(
        string='API Token JSON.PE',
        config_parameter='json_pe.api_token',
        help='Token de autenticación para la API de json.pe. '
             'Obtén tu token en https://json.pe',
        required=False,
    )
