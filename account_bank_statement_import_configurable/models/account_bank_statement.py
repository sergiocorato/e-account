# -*- coding: utf-8 -*-
# Copyright 2019 Sergio Corato (https://efatto.it)

from odoo import models, fields, api


class ResBank(models.Model):
    _inherit = "res.bank"

    init_line_to_exclude = fields.Integer('Initial lines to exclude')
    end_line_to_exclude = fields.Integer('End lines to exclude')
    column_header = fields.Char(
        'Column header', help='List of column headers separated by "," '
                              'and with this format: '
                              'column_field:column_name:column_type'
                              'Where column_field is the db field, '
                              'column_name is the csv field '
                              'and column type is the db type.')
    separator = fields.Selection([
        (',', "Comma"),
        (';', "Semicolon"),
        ('\t', "Tab"),
        (' ', "Space")
    ], string="Separator")
    float_thousand_separator = fields.Selection([
        (',', "Comma"),
        ('.', "Dot"),
    ], string="Thousand separator")
    float_decimal_separator = fields.Selection([
        (',', "Comma"),
        ('.', "Dot"),
    ], string="Decimal separator")
    date_format = fields.Char('Date format')
    debit_column_pos = fields.Integer('Debit column position')
    credit_column_pos = fields.Integer('Credit column position')
    abi_reason_column_pos = fields.Integer('ABI reason position')


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    bank_init_line_to_exclude = fields.Integer('Initial lines to exclude')
    bank_end_line_to_exclude = fields.Integer('End lines to exclude')
    bank_column_header = fields.Char(
        'Column header', help='List of column headers separated by "," '
                              'and with this format: '
                              'column_field:column_name:column_type'
                              'Where column_field is the db field, '
                              'column_name is the csv field '
                              'and column type is the db type.')
    bank_separator = fields.Selection([
        (',', "Comma"),
        (';', "Semicolon"),
        ('\t', "Tab"),
        (' ', "Space")
    ], string="Separator")
    bank_float_thousand_separator = fields.Selection([
        (',', "Comma"),
        ('.', "Dot"),
    ], string="Thousand separator")
    bank_float_decimal_separator = fields.Selection([
        (',', "Comma"),
        ('.', "Dot"),
    ], string="Decimal separator")
    bank_date_format = fields.Char('Date format')
    bank_debit_column_pos = fields.Integer('Debit column position')
    bank_credit_column_pos = fields.Integer('Credit column position')
    bank_abi_reason_column_pos = fields.Integer('ABI reason position')

    @api.onchange('bank_id')
    def onchange_bank_id(self):
        if self.bank_id:
            self.bank_init_line_to_exclude = self.bank_id.init_line_to_exclude
            self.bank_end_line_to_exclude = self.bank_id.end_line_to_exclude
            self.bank_column_header = self.bank_id.column_header
            self.bank_separator = self.bank_id.separator
            self.bank_date_format = self.bank_id.date_format
            self.bank_float_thousand_separator = \
                self.bank_id.float_thousand_separator
            self.bank_float_decimal_separator = \
                self.bank_id.float_decimal_separator
            self.bank_debit_column_pos = self.bank_id.debit_column_pos
            self.bank_credit_column_pos = self.bank_id.credit_column_pos
            self.bank_abi_reason_column_pos = \
                self.bank_id.abi_reason_column_pos
