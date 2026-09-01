from odoo import fields, models, api


class CourseCenterInstructor(models.Model):
    _name = 'course_center.instructor'
    _description = 'Instructor'
    _rec_name = 'user_id'

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=True
    )

    specialization = fields.Char(string='Specialization')

    hire_date = fields.Date(
        string='Hire Date',
        required=True,
        default=lambda self: fields.Date.today()
    )