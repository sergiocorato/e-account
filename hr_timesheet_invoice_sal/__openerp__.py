# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 Sergio Corato
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Hr timesheet invoice sal',
    'version': '8.0.1.0.0',
    'category': 'Extra Tools',
    'description':
        'Hr timesheet invoice sal',
    'author': 'Sergio Corato',
    'website': 'http://www.efatto.it',
    'depends': [
        'hr_timesheet_invoice',
        'account_analytic_sal',
    ],
    'data': [
        'views/hr_timesheet.xml',
    ],
    'installable': True,
}