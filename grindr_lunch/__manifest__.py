{
    'name': 'Grindr Lunch',
    'summary': 'An apple a day keeps the doctor away',
    'description':
    """
        developed by: jrbr-odoo, erga-odoo, jden-odoo
    """,
    'author': 'Odoo Development Services',
    'maintainer': 'Odoo Development Services',
    'website': 'https://www.odoo.com',
    'category': 'Custom Development',
    'version': '1.0.0',
    'license': 'OPL-1',
    'depends': ['lunch', 'survey', 'hr'],
    'data': [
        "views/survey_survey_views.xml",
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/res_partner.xml',
        'views/survey_wizard_form.xml'
    ],
}
