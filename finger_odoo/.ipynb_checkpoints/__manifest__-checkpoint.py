# -*- coding: utf-8 -*-
{
    'name': "finger_odoo",

    'summary': """
        this module to add field name device id to connect Finger print with odoo """,

    'description': """
            this module to add field name device id to connect Finger print with odoo
    """,

    'author': "EgyMentors@Muhammed Ashraf",
    'website': "https://www.egymentors.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Modules/Human Resources',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
   'license': 'AGPL-3',
   'installable': True,
   'auto_install': False,
   'application': False,
}
