# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	sale_status = fields.Selection([
									('critical', 'Critical'),
									('defaulted', 'Defaulted'),
									('no_risk', 'No risk')
					],
					compute='_get_sale_status',
					string='Sale Status'
				)

	@api.depends('date_order', 'amount_total')
	def _get_sale_status(self):
		for record in self:
			paid_amount = 0.0
			sale_status = 'no_risk'

			duration = (datetime.today() - record.date_order).days

			if record.invoice_ids:
				for rec in record.invoice_ids:
					paid_amount += rec.amount_total - rec.amount_residual

			if duration > 19 and duration < 50:
				if paid_amount < (record.amount_total * 5) / 100:
					sale_status = 'critical'
				else:
					sale_status = 'no_risk'

			if duration > 49 and duration < 100:
				if paid_amount < (record.amount_total * 50) / 100:
					sale_status = 'critical'
				else:
					sale_status = 'no_risk'

			if duration >= 100:
				if paid_amount < record.amount_total:
					sale_status = 'defaulted'
				else:
					sale_status = 'no_risk'

			record.sale_status = sale_status


