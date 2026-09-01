from odoo import fields, models, api


class CourseCenterPayment(models.Model):
    _name = 'course_center.payment'
    _rec_name = 'invoice_id'

    invoice_id = fields.Many2one(
        comodel_name='course_center.invoice',
        string='Invoice',
        required=True
    )

    payment_date = fields.Date(
        string='Payment Date',
        required=True,
        default=lambda self: fields.Date.today()
    )

    amount = fields.Float(
        string='Amount',
        digits=(12, 2),
        required=True
    )

    payment_method = fields.Selection(
        string='Payment Method',
        required=True,
        selection=[
            ('cash', 'Cash'),
            ('card', 'Card'),
            ('bank_transfer', 'Bank Transfer')
        ]
    )

    status = fields.Selection(
        string='Status',
        required=True,
        default='completed',
        selection=[
            ('completed', 'Completed'),
            ('failed', 'Failed'),
            ('refunded', 'Refunded')
        ]
    )

    notes = fields.Char(string='Notes')