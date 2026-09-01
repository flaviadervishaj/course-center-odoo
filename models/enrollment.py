from odoo import fields, models, api


class CourseCenterEnrollment(models.Model):
    _name = 'course_center.enrollment'

    student_id = fields.Many2one(
        comodel_name='course_center.student',
        string='Student',
        required=True
    )

    group_id = fields.Many2one(
        comodel_name='course_center.group',
        string='Course Group',
        required=True
    )

    rule_id = fields.Many2one(
        comodel_name='course_center.discount_rule',
        string='Discount Rule'
    )

    enrollment_date = fields.Date(
        string='Enrollment Date',
        required=True,
        default=lambda self: fields.Date.today()
    )

    status = fields.Selection(
        string='Status',
        required=True,
        default='pending',
        selection=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ]
    )

    original_price = fields.Float(
        string='Original Price',
        digits=(12, 2)
    )

    discount_amount = fields.Float(
        string='Discount Amount',
        digits=(12, 2)
    )

    final_price = fields.Float(
        string='Final Price',
        digits=(12, 2)
    )

    payment_plan = fields.Selection(
        string='Payment Plan',
        required=True,
        default='full',
        selection=[
            ('full', 'Full Payment'),
            ('monthly', 'Monthly Payment')
        ]
    )

    notes = fields.Char(string='Notes')

    @api.depends('student_id', 'group_id')
    def _compute_display_name(self):
        for record in self:
            student_name = record.student_id.user_id.name or ''
            group_name = record.group_id.group_name or ''

            if student_name and group_name:
                record.display_name = f"{student_name} - {group_name}"
            elif student_name:
                record.display_name = student_name
            else:
                record.display_name = 'Enrollment'

    @api.onchange('group_id', 'rule_id')
    def _onchange_price(self):
        if self.group_id:
            self.original_price = self.group_id.course_id.price

            if self.rule_id:
                self.discount_amount = (
                    self.original_price
                    * self.rule_id.discount_percentage
                    / 100
                )
            else:
                self.discount_amount = 0

            self.final_price = (
                self.original_price - self.discount_amount
            )