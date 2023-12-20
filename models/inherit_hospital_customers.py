from odoo import fields , models, api
from odoo.exceptions import  ValidationError, UserError
class Hospital_customers(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('patient')



    # @api.constrains('related_patient_id')
    # def valid_related_patient(self):
    #     for rec in self:
    #         patient_id = rec.search([('related_patient_id', '=', rec.related_patient_id.id)])
    #         if len(patient_id) > 1:
    #             raise ValidationError('This patient is already related to a different customer.')

    @api.constrains('related_patient_id')
    def valid_related_patient(self):
        for rec in self:
            patient_id = rec.search([('related_patient_id', '=', rec.related_patient_id.id), ('id', '!=', rec.id)])
            if patient_id:
                raise ValidationError('This patient is already related to a different customer.')


        
    def unlink(self):
        for rec in self :
            if rec.related_patient_id:
                raise UserError('This customer is linked to patient')
            else :
                super.unlink()
            

