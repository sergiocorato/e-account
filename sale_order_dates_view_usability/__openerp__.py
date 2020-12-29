# -*- coding: utf-8 -*-
#
#
#    Copyright (C) 2017 Sergio Corato
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{
    'name': 'Sale order dates view usability',
    'version': '8.0.2.0.0',
    'category': 'other',
    'author': 'Sergio Corato',
    'description': 'This module move sale order ref in tree view after '
                   'partner, compute requested date on date of confirmation + '
                   '"sale_default_lead_days" if present in parameters and '
                   'change calendar view basing it on date requested.',
    'website': 'http://www.efatto.it',
    'license': 'AGPL-3',
    'depends': [
        'calendar',
        'sale_order_dates',
        'sale_order_line_date',
    ],
    'data': [
        'views/calendar.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True
}