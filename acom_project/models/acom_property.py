from odoo import fields,models

class AcomPropertyModel(models.Model):
    _inherit = "acom.property.model"

    def action_create_project(self):
        vals={
            'partner_id':self.propOwner.id,
            'name':self.name,
            'task_ids':[
                fields.Command.create({
                    "name":"Maintainence"
                })
            ]
        }
        self.env['project.project'].create(vals)
        return super(AcomPropertyModel,self)
