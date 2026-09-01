from odoo import fields, models, api


class CourseCenterAssignment(models.Model):
    _name = 'course_center.assignment'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)

    group_id = fields.Many2one(
        comodel_name='course_center.group',
        string='Course Group',
        required=True
    )

    description = fields.Char(string='Description')

    type = fields.Selection(
        string='Type',
        required=True,
        default='assignment',
        selection=[
            ('assignment', 'Assignment'),
            ('project', 'Project'),
            ('exam', 'Exam')
        ]
    )

    deadline = fields.Datetime(
        string='Deadline',
        required=True
    )

    publish_date = fields.Date(
        string='Publish Date',
        default=lambda self: fields.Date.today()
    )

    status = fields.Selection(
        string='Status',
        required=True,
        default='draft',
        selection=[
            ('draft', 'Draft'),
            ('published', 'Published'),
            ('closed', 'Closed')
        ]
    )

    created_at = fields.Datetime(
        string='Created At',
        default=lambda self: fields.Datetime.now()
    )

    def publish_assignment(self):
        self.status = 'published'

    def close_assignment(self):
        self.status = 'closed'