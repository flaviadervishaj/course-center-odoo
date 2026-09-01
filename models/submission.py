from odoo import fields, models, api


class CourseCenterSubmission(models.Model):
    _name = 'course_center.submission'
    _rec_name = 'assignment_id'

    assignment_id = fields.Many2one(
        comodel_name='course_center.assignment',
        string='Assignment',
        required=True
    )

    enrollment_id = fields.Many2one(
        comodel_name='course_center.enrollment',
        string='Enrollment',
        required=True
    )

    submission_date = fields.Datetime(
        string='Submission Date',
        required=True,
        default=lambda self: fields.Datetime.now()
    )

    file_path = fields.Char(string='File Path')
    comments = fields.Char(string='Comments')
    grade = fields.Float(string='Grade')
    feedback = fields.Char(string='Feedback')

    graded_at = fields.Datetime(string='Graded At')

    graded_by = fields.Many2one(
        comodel_name='course_center.instructor',
        string='Graded By'
    )

    status = fields.Selection(
        string='Status',
        required=True,
        default='submitted',
        selection=[
            ('submitted', 'Submitted'),
            ('graded', 'Graded')
        ]
    )

    is_late = fields.Boolean(
        string='Late Submission',
        compute='_calc_is_late'
    )

    @api.depends('submission_date', 'assignment_id.deadline')
    def _calc_is_late(self):
        for submission in self:
            submission.is_late = False

            if (
                submission.submission_date
                and submission.assignment_id.deadline
            ):
                submission.is_late = (
                    submission.submission_date
                    > submission.assignment_id.deadline
                )

    def grade_submission(self):
        self.status = 'graded'
        self.graded_at = fields.Datetime.now()