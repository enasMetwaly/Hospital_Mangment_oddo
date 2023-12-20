from odoo import fields ,models, api
from odoo.exceptions import  ValidationError
from datetime import date
import re

class Patient(models.Model):
    
    _name ='patient'
    _rec_name ="first_name"
    first_name = fields.Char()
    last_name = fields.Char()
    birth_day = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([('A+', 'A+'),('A-', 'A-'),('B+', 'B+'),('B-', 'B-'),('AB+', 'AB+'),('AB-', 'AB-'),('O+', 'O+'),('O-', 'O-')])
    PCR = fields.Boolean()
    image = fields.Image()
    address = fields.Char()
    age = fields.Integer(compute ='_compute_age', store = True)
    email = fields.Char()

    states= fields.Selection([("state1","Undetermined"),("state2","Good"),("state3","Fair"),("state4","Serious")])
    department = fields.Many2one(comodel_name='hms.department' ) 
    department_capacity= fields.Integer(related='department.capacity')
     
    doctors= fields.Many2many(comodel_name='hms.doctors')


    states_logs = fields.One2many('patient.states.logs' , 'patient_id')


    @api.onchange('age')
    def pcr_checked(self) :
        for rec in self:
            if rec.age < 30 :
                rec.PCR = True
                return{
                    'warning':{
                        'title':('Age changed') ,
                        'message': 'PCR field has been checked because age less than 30 and must fill CR ratio'
                    }
                }  

    @api.onchange('states')
    def create_states_log(self):
        for rec in self:
            vals = {
                'description': f'State changed to {rec.states}',
                'patient_id': rec.id
            }
            rec.env['patient.states.logs'].create(vals)

    # @api.constrains('age')
    # def check_age(self):
    #     for rec in self:
    #         if rec.age < 0 :
    #             raise ValidationError('Age can\'t be less than zero')

    @api.depends('birth_day')
    def _compute_age(self):
        for rec in self:

            if rec.birth_day:
                today = date.today()
                rec.age = today.year - rec.birth_day.year - (
                        (today.month, today.day) < (rec.birth_day.month, rec.birth_day.day))
                if rec.age < 0 :
                    raise ValidationError('Age can\'t be less than zero')
                
    @api.constrains('email')
    def _vaild_name(self) :
        for rec in self :
            regex =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not rec.email :
                raise Exception("you must provide email address")
            elif not re.match(regex, rec.email) :
                raise ValidationError("email is not vaild")

    _sql_constraints = [
        ('unique_patient_email' , 'UNIQUE(email)' , 'your email should be unique')
    ]

