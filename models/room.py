from odoo import fields,models,api

class Room(models.Model):
    _name = 'course_center.room'

    name = fields.Char(string='Room Name')
    capacity = fields.Integer(string='Capacity')

    status = fields.Selection([
        ('active','Active'),
        ('inactive','Inactive'),
    ], string='Status' , default='active' )