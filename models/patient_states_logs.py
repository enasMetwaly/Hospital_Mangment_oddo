from odoo import fields, models, api


class patient_logs(models.Model):

    _name ='patient.states.logs'

    description = fields.Char(required=True)
    patient_id =fields.Many2one('patient')