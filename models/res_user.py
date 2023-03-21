from odoo import fields,models

class ResUsers(models.Model):
    _inherit = 'res.users'

    acomProperty_ids = fields.One2many('acom.property.model','propManager_id')
    salary = fields.Integer(string="Salary")