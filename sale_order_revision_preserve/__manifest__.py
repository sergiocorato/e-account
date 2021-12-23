# Copyright 2021 Sergio Corato <https://github.com/sergiocorato>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Sale order revision preserve',
    'version': '12.0.1.0.0',
    'category': 'Sale Management',
    'author': 'Sergio Corato',
    'description': 'This module add logic to store a copy of sale order as revision, '
                   'while the user continue to use the same sale order, to preserve '
                   'chat history and attachments.',
    'website': 'https://efatto.it',
    'depends': [
        'sale_order_revision',
    ],
    'data': [
    ],
    'installable': True,
}
