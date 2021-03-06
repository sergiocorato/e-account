from odoo import models, fields, api, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('partner_id')
    def _partner_id_onchange(self):
        if self.partner_id:
            if self.partner_id.customer:
                self.account_id = self.partner_id.property_account_receivable_id
            elif self.partner_id.supplier:
                self.account_id = self.partner_id.property_account_payable_id

    @api.onchange('credit')
    def _credit_onchange(self):
        if self.credit and self.debit:
            self.debit = 0

    @api.onchange('debit')
    def _debit_onchange(self):
        if self.debit and self.credit:
            self.credit = 0

    name = fields.Text('Name', required=True)
    date_from = fields.Date(
        compute=lambda *a, **k: {},
        string="Date from")
    date_to = fields.Date(
        compute=lambda *a, **k: {},
        string="Date to")

    @api.model
    def default_get(self, fields):
        data = super(AccountMoveLine, self).default_get(fields)
        if data and self._context.get('line_ids', False):
            debit = credit = 0
            for x in self._context['line_ids']:
                debit += x[2]['debit'] if x[2] and x[2].get('debit') else 0
            for x in self._context['line_ids']:
                credit += x[2]['credit'] if x[2] and x[2].get('credit') else 0
            balance = credit - debit
            if balance > 0:
                data['debit'] = balance
            elif balance < 0:
                data['credit'] = abs(balance)
        return data
