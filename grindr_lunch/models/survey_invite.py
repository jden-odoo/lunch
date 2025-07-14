from odoo import models, fields, api


class SurveyInvite(models.TransientModel):
    _inherit = 'survey.invite'

    deadline = fields.Datetime(related='survey_id.date_deadline')

    @api.onchange('send_email')
    def _compute_partner_ids(self):
        BUFFALO_OFFICE = self.env.ref('grindr_lunch.buffalo_office')
        self.partner_ids = self.env['hr.employee'].search([('work_location_id', '=', BUFFALO_OFFICE.id)]).mapped('work_contact_id')
