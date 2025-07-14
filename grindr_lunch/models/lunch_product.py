from odoo import fields, models


class LunchProduct(models.Model):
    _inherit = 'lunch.product'

    category_id = fields.Many2one(required=False)
    supplier_id = fields.Many2one(required=False)
