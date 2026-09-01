from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    course_center_role = fields.Selection(
        string='Course Center Role',
        selection=[
            ('administrator', 'Administrator'),
            ('instructor', 'Instructor'),
            ('student', 'Student')
        ]
    )