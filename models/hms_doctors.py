from odoo import fields ,models

class Doctors(models.Model):

    _name ='hms.doctors'
    _rec_name ="first_name"
    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Image()
    department = fields.Many2many(comodel_name="hms.department")

