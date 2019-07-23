# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_trainer = fields.Boolean("Is Trainer")
    is_attendee = fields.Boolean("Is Attendee")