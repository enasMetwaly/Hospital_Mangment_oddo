from odoo import fields ,models

class Department(models.Model):

    _name ='hms.department'
    _rec_name ="name"
    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient = fields.One2many('patient' ,'department')
    doctors =fields.Many2many(comodel_name='hms.doctors')