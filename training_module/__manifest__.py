# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Training',
    'version' : '1.1',
    'summary': 'Training and Attendee',
    'sequence': 15,
    'description': """
        Training Module
    """,
    'category': '',
    'website': 'www.on.net.my',
    'images' : [],
    'depends' : ['base','contacts'],
    'data': [
        'views/res_partner_view.xml',
        'views/training_view.xml',
        'views/course_view.xml',
        'security/ir.model.access.csv',
        'report/training_report.xml',
        'report/training_report_template.xml',

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
