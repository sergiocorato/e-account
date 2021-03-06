from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    country_id = fields.Many2one(
        related='partner_id.country_id'
    )
