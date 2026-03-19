# -*- coding: utf-8 -*-
{
    'name': 'Master_data',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Adding Master Data',
    'depends': ['purchase', 'stock','product'],
    'data': [

        'views/menu.xml',
        'views/business_unit_views.xml',
        
    ],
    'installable': True,
    
    'sequence': -10,
    'application':True,
    'author':'Hein Thura San',
    
    
    'license':'LGPL-3',
}