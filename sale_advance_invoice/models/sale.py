# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields, api, _


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.model
    def _get_order_lines(self):
        line_ids = self.env['sale.order'].browse(
            self._context['active_id']).order_line
        return line_ids

    order_line_ids = fields.Many2many(
        comodel_name='sale.order.line',
        relation='advance_sale_order_line_rel',
        column1='order_line_id', column2='advance_id',
        string='Order lines',
        default=_get_order_lines,
        help='Select order lines to print details in invoice'
    )

    @api.multi
    def create_invoices(self):
        """ create invoices for the active sales orders """
        if self.advance_payment_method in ('fixed', 'percentage'):
            inv_ids = []
            for sale_id, inv_values in self._prepare_advance_invoice_vals():
                inv_ids.append(self._create_invoices(inv_values, sale_id))
            for inv in self.env['account.invoice'].browse(inv_ids):
                if self.order_line_ids:
                    description = ''
                    for line in self.order_line_ids:
                        description += ('\n' + line.name)
                for invoice_line in inv.invoice_line:
                    invoice_line.name += description
            if self._context.get('open_invoices', False):
                return self.open_invoices(inv_ids)
            return {'type': 'ir.actions.act_window_close'}
        else:
            return super(SaleAdvancePaymentInv, self).create_invoices()