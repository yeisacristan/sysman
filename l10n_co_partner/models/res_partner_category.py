# -*- coding: utf-8 -*-
# Copyright 2024 Alejandro Olano ( Sysman SAS), jaramirez@sysman.com.co

from odoo import models, api
from odoo.exceptions import ValidationError


class ResPartnerCategory(models.Model):
    _inherit = "res.partner.category"

    @api.model
    def create(self, values):
        if values.get("name") == "partner_categ":
            return super().create(values)
        category = self.env["res.partner.category"].search([("name", "=", values.get("name"))])
        if category:
            raise ValidationError("Ya Existe la Etiqueta %s en la Base de Datos" % (values.get("name")))
        return super().create(values)
