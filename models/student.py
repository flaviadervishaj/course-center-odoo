from odoo import fields, models, api

class Student(models.Model):
    _name = 'course_center.student'

    user_id = fields.Many2one(
        'res.users',
        string='User'
    )

    date_of_birth = fields.Date(string='Date of Birth')
    address = fields.Char(string='Address')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')

    registration_date = fields.Date(
        string='Registration Date'
    )