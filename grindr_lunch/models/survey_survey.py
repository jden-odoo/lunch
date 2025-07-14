from odoo import models, fields, api, _


class Survey(models.Model):
    _inherit = 'survey.survey'

    date_deadline = fields.Datetime(string='Deadline')

    @api.model
    def _cron_close_survey(self):
        self.search([('date_deadline', '<', fields.Datetime.today())]).action_archive()

    def action_lunch_wizard(self):
        self.ensure_one()
        item_vals = []
        for day in range(1, 6):
            for option in ['regular', 'gluten_free', 'vegetarian', 'vegan']:
                item_vals.append({
                    'dietary_type': option,
                    'day': str(day),
                })
        items = self.env['lunch.item'].sudo().create(item_vals)
        return {
                'name': _('Create Lunch Menu'),
                'type': 'ir.actions.act_window',
                'view_mode': 'list',
                'res_model': 'lunch.item',
                'target': 'new',
                'domain': [('id', 'in', items.ids)],
                'context': {'survey_id': self.id, 'group_by': ['day', 'dietary_type']}
        }
