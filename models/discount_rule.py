from odoo import fields, models, api


class CourseCenterDiscountRule(models.Model):
    _name = 'course_center.discount_rule'
    _rec_name = 'description'

    course_number = fields.Integer(
        string='Course Number',
        required=True
    )

    discount_percentage = fields.Float(
        string='Discount Percentage',
        required=True
    )

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