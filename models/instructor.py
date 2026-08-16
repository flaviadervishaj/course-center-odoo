from odoo import fields, models,api
class instructor(models.Model):
    _name = 'course_center.instructor'

    instructor_id = fields.Many2one(
        'res.users',
        string='User',
    )

    specialization = fields.Char(string='Specialization')
    hire_date = fields.Date(string='Hire Date')
