# -*- coding: utf-8 -*-
{
    'name'          : "Sale Extension",
    'summary'       : "Extension of Sale Module",
    'description'   : """ This module add region and geodata fields in contacts form view /
                        Allows sale status management / 
                        Add 100 Days payment term 
                      """,
    'author'        : "Thierno Mamadou Diallo",
    'website'       : "http://www.pegafrica.com",
    'category'      : 'Sale',
    'version'       : '14.0.1',
    'depends'       : ['sale'],

    'data'          : [
                        'security/ir.model.access.csv',
                        'views/sale_order.xml',
                        'views/contacts.xml',
                        'data/payment_terms.xml'
                    ],
}