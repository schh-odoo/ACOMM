from odoo import fields,models

class AcomTenantModel(models.Model):
    _inherit="acom.tenant.model"

    def action_create_invoice(self):
        vals={
            'invoice_partner_display_name':self.name,
            'invoice_date':fields.date.today(),
            'move_type':'out_invoice',
            'invoice_line_ids':[
                fields.Command.create({
                    'name':self.name,
                    'quantity':1,
                    'price_unit':self.rent
                }),
                fields.Command.create({
                    'name':'admin fees',
                    'quantity':1,
                    'price_unit':100
                })
            ]
        }
        self.env["account.move"].create(vals)
        return super(AcomTenantModel,self)