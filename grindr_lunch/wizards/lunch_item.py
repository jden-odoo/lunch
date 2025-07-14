from odoo import models, fields
from odoo import Command


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
        day_of_week = {
            '1': 'Monday',
            '2': 'Tuesday',
            '3': 'Wednesday',
            '4': 'Thursday',
            '5': 'Friday',
        }
        dietary_type_formatted = {
            'gluten_free': 'Gluten Free',
            'vegetarian': 'Vegetarian',
            'vegan': 'Vegan',
            'regular': 'Regular',
        }
        survey = self.env['survey.survey'].search([('id', '=', self.env.context.get('survey_id'))])
        records_by_day = [self.filtered(lambda rec: int(rec.day) == d) for d in range(1, 6)]
        for menu_items_per_day in records_by_day:
            if menu_items_per_day:
                self.env['survey.question'].create({
                    'survey_id': survey.id,
                    'title': day_of_week[menu_items_per_day[0].day],
                    'sequence': 1,
                    'question_type': 'simple_choice',
                    'suggested_answer_ids': [Command.create({
                        'value': f"{dietary_type_formatted[line.dietary_type]}: {line.product_id.name}"
                    }) for line in menu_items_per_day],
                })
