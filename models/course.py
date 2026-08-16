from odoo import fields, models, api

class Course(models.Model):
    _name = 'course_center.course'

    category_id = fields.Many2one(
        'course_center.category',
        string='Category',
    )
    