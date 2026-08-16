from odoo import fields, models, api


class CourseCategory(models.Model):
    _name = 'course_center.category'

    name = fields.Char(string='Category Name')
    description = fields.Char(string='Description')

    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Status', default='active')
