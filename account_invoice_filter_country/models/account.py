from odoo import fields, models


class AccountInvoice(models.Model):
    _inherit = "account.move"

    country_id = fields.Many2one(related="partner_id.country_id")
