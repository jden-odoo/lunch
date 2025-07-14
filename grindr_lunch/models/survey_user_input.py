# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    def create(self,vals_list):
        # Unlink existing answers for the same survey and email
        self.env['survey.user_input'].search( 
            ["&", ("survey_id", "=", vals_list[0].get('survey_id')), ("email", "=", vals_list[0].get('email'))]
        ).unlink()
        return super(SurveyUserInput, self).create(vals_list)
        