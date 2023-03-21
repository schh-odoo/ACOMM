{
    'name': "A-Com",
    'depends':['base'],
    'version': '1.0',
    'sequence': -101,
    'author': 'sankalp (schh)',
    'category': 'Management',
    'installable': True,
    'application':True,
    'license': 'LGPL-3',
    'summary': 'Application to manage your accommodation business',
    'data': [
        'security/ir.model.access.csv',
        'views/acom_locations_view.xml',
        'views/acom_properties_view.xml',
        'views/acom_rooms_view.xml',
        'views/acom_tenant_view.xml',
        'views/res_users_views.xml',
        'views/acom_menu.xml',
        'data/master_data.xml'
    ],
    'demo':[
        'demo/demo_data.xml'
    ]
}
