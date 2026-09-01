from odoo import fields, models, api


class CourseCenterRoom(models.Model):
    _name = 'course_center.room'

    name = fields.Char(string='Room Name', required=True)
    capacity = fields.Integer(string='Capacity')

    status = fields.Selection(
        string='Status',
        required=True,
        default='active',
        selection=[
            ('active', 'Active'),
            ('inactive', 'Inactive')
        ]
    )