
from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    discount = fields.Float()

    @api.multi
    @api.depends('discount', 'invoice_line_ids')
    def invoice_discount_update(self):
        for invoice in self:
            invoice.invoice_line_ids.filtered(
                lambda x: x.product_id.type != 'service'
            ).write({'discount': invoice.discount})
