from odoo import models, fields


class LunchItem(models.TransientModel):
    _name = 'lunch.item'

    day = fields.Selection(selection=[
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday')
    ], required=True)
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    dietary_type = fields.Selection(selection=[
        ('gluten_free', 'Gluten Free'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('regular', 'Regular')
    ])
    product_id = fields.Many2one(comodel_name='lunch.product')

    def action_create_lines(self):
        pass