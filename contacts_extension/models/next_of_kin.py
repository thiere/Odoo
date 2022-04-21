# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class next_of_kin(models.Model):
    _name = 'next.kin'
    _description = 'Contacts Next of Kin'

    first_name = fields.Char('First name', required=True)
    last_name = fields.Char('Last name', required=True)
    date_of_birth = fields.Date('Date of Birth')
    age = fields.Integer(compute='_compute_age', string='Age')
    employee_id = fields.Many2one('res.partner', string='Contact')
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            age = 0
            if record.date_of_birth:
                birth_date = datetime.strptime(str(record.date_of_birth), '%Y-%m-%d')
                age = (datetime.today() - birth_date).days / 365
            record.age = age

class Contacts(models.Model):
    _inherit = 'res.partner'

    next_of_kin_ids = fields.One2many(
        'next.kin', 
        'employee_id', 
        string='Next of Kin', 
        groups="contacts_extension.goup_family_manager"
    )