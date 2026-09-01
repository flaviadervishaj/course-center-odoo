from odoo import fields, models, api


class CourseCenterSession(models.Model):
    _name = 'course_center.session'
    _rec_name = 'topic'

    group_id = fields.Many2one(
        comodel_name='course_center.group',
        string='Course Group',
        required=True
    )

    room_id = fields.Many2one(
        comodel_name='course_center.room',
        string='Room',
        required=True
    )

    session_date = fields.Date(
        string='Session Date',
        required=True
    )

    start_time = fields.Float(
        string='Start Time',
        required=True
    )

    end_time = fields.Float(
        string='End Time',
        required=True
    )

    topic = fields.Char(string='Topic', required=True)

    status = fields.Selection(
        string='Status',
        required=True,
        default='scheduled',
        selection=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ]
    )