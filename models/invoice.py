from odoo import fields, models, api


class CourseCenterInvoice(models.Model):
    _name = 'course_center.invoice'
    _rec_name = 'enrollment_id'

    enrollment_id = fields.Many2one(
        comodel_name='course_center.enrollment',
        string='Enrollment',
        required=True
    )

    invoice_date = fields.Date(
        string='Invoice Date',
        required=True,
        default=lambda self: fields.Date.today()
    )

    due_date = fields.Date(
        string='Due Date',
        required=True
    )

    status = fields.Selection(
        string='Status',
        required=True,
        default='draft',
        selection=[
            ('draft', 'Draft'),
            ('open', 'Open'),
            ('paid', 'Paid'),
            ('cancelled', 'Cancelled')
        ]
    )

    notes = fields.Char(string='Notes')

    payment_ids = fields.One2many(
        comodel_name='course_center.payment',
        inverse_name='invoice_id',
        string='Payments'
    )

    def open_invoice(self):
        self.status = 'open'

    def pay_invoice(self):
        self.status = 'paid'

    def cancel_invoice(self):
        self.status = 'cancelled'