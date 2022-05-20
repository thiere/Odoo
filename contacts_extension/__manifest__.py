# -*- coding: utf-8 -*-
{
    'name'          : "Contacts Extension",
    'summary'       : "Extension of Contacts Module",
    'description'   : """ 
                        This modules allows authorized users to store contacts Next of Kin test github desktop
                      """,
    'author'        : "Thierno Mamadou Diallo",
    'website'       : "http://www.pegafrica.com",
    'category'      : 'Contacts',
    'version'       : '14.0.1',
    'depends'       : ['contacts'],

    'data'          : [
                        'security/groups.xml',
                        'security/ir.model.access.csv',
                        'views/next_of_kin.xml',
                    ],
}

