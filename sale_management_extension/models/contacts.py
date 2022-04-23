# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Contacts(models.Model):
	_inherit = 'res.partner'

	region = fields.Many2one('contact.region', 'Region')
	geodata = fields.Char('Geo data')

class contact_region(models.Model):
	_name = 'contact.region'
	_description = 'Region of the Contact'

	name = fields.Char('Region name')