from odoo import fields, models, api


class CourseCenterAttendance(models.Model):
    _name = 'course_center.attendance'
    _rec_name = 'enrollment_id'

    session_id = fields.Many2one(
        comodel_name='course_center.session',
        string='Course Session',
        required=True
    )

    enrollment_id = fields.Many2one(
        comodel_name='course_center.enrollment',
        string='Enrollment',
        required=True
    )

    status = fields.Selection(
        string='Status',
        required=True,
        default='present',
        selection=[
            ('present', 'Present'),
            ('absent', 'Absent'),
            ('late', 'Late')
        ]
    )

    notes = fields.Char(string='Notes')