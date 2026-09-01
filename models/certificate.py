from odoo import fields, models, api


class CourseCenterCertificate(models.Model):
    _name = 'course_center.certificate'
    _rec_name = 'certificate_number'

    enrollment_id = fields.Many2one(
        comodel_name='course_center.enrollment',
        string='Enrollment',
        required=True
    )

    certificate_number = fields.Char(
        string='Certificate Number',
        required=True
    )

    issue_date = fields.Date(
        string='Issue Date',
        required=True,
        default=lambda self: fields.Date.today()
    )

    file_path = fields.Char(string='File Path')