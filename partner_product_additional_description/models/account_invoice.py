# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def get_partner_product_additional_description(self):
        for invoice in self:
            if not invoice.partner_id.is_company:
                invoice.partner_product_additional_description_id = \
                    invoice.partner_id.parent_id.\
                    partner_product_additional_description_id
            else:
                invoice.partner_product_additional_description_id = \
                    invoice.partner_id.\
                    partner_product_additional_description_id

    partner_product_additional_description_id = fields.Many2one(
        comodel_name='product.additional.description',
        compute=get_partner_product_additional_description,
    )
