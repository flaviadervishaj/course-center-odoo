from odoo import fields, models, api


class CourseCenterGroup(models.Model):
    _name = 'course_center.group'
    _rec_name = 'group_name'

    group_name = fields.Char(string='Group Name', required=True)

    course_id = fields.Many2one(
        comodel_name='course_center.course',
        string='Course',
        required=True
    )

    instructor_id = fields.Many2one(
        comodel_name='course_center.instructor',
        string='Instructor',
        required=True
    )

    capacity = fields.Integer(string='Capacity')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

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
