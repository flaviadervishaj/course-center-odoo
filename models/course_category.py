from odoo import fields, models, api


class CourseCenterCategory(models.Model):
    _name = 'course_center.category'
    _description = 'Course Category'

    name = fields.Char(string='Category Name')
    description = fields.Char(string='Description')

    status = fields.Selection(
        string='Status',
        required=True,
        default='active',
        selection=[
            ('active', 'Active'),
            ('inactive', 'Inactive')
        ]
    )