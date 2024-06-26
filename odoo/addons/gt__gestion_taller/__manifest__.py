# -*- coding: utf-8 -*-
{
    'name': "GT_GestionTaller",

    'summary': """
        Gestion del taller simplificada""",

    'description': """
        Módulo para la ayuda a la gestión de un taller
    """,

    'author': "Gustavo Puentes",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/clientes.xml',
        'views/ordenes.xml',
        'views/trabajadores.xml',
        'views/piezas.xml',
        'views/citas.xml',
        'views/vehiculos.xml',
        'views/menus.xml',
        'reports/report.xml',
        'reports/report_order.xml',
        'reports/factura_order.xml',
        # 'data/mail_template.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/vehiculos_demo.xml',
        'demo/piezas_demo.xml',
        'demo/trabajadores_demo.xml',
        'demo/clientes_demo.xml',
        'demo/ordenes_demo.xml',
    ],
    'application': True,
    'installable': True,
}