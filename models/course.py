from odoo import fields, models, api


class CourseCenterCourse(models.Model):
    _name = 'course_center.course'

    name = fields.Char(string='Course Name', required=True)

    category_id = fields.Many2one(
        comodel_name='course_center.category',
        string='Category',
        required=True
    )

    description = fields.Char(string='Description')
    total_hours = fields.Float(string='Total Hours')
    duration_weeks = fields.Integer(string='Duration Weeks')
    price = fields.Float(string='Price', digits=(12, 2))

    certificate_min_points = fields.Float(
        string='Minimum Certificate Points',
        default=30
    )