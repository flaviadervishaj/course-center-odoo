from odoo import fields, models, api


class CourseCenterStudent(models.Model):
    _name = 'course_center.student'
    _rec_name = 'user_id'

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=True
    )

    date_of_birth = fields.Date(string='Date of Birth')
    address = fields.Char(string='Address')

    gender = fields.Selection(
        string='Gender',
        selection=[
            ('female', 'Female'),
            ('male', 'Male'),
            ('other', 'Other')
        ]
    )

    registration_date = fields.Date(
        string='Registration Date',
        required=True,
        default=lambda self: fields.Date.today()
    )