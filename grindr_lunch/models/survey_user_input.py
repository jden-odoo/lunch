# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    def create(self,vals_list):
        if isinstance(vals_list, list):
            for val in vals_list:
                self.env['survey.user_input'].search(
                    ["&", ("survey_id", "=", vals_list[val].get('survey_id')), ("email", "=", vals_list[val].get('email'))]
                ).unlink()
        else:
            self.env['survey.user_input'].search(
                ["&", ("survey_id", "=", vals_list.get('survey_id')), ("email", "=", vals_list.get('email'))]
            ).unlink()
        return super(SurveyUserInput, self).create(vals_list)
