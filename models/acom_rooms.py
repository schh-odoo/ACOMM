from odoo import models, fields,api,exceptions

class AcomRoomsModel(models.Model):
    _name = "acom.rooms.model"
    _description = "Each Room Model"
    _rec_name="roomNumber"
    
    roomNumber = fields.Integer()
    currentCap = fields.Integer(readonly=True,compute="_compute_current_cap")
    maxCap = fields.Integer(readonly=True,compute="_compute_max_cap")
    # perHeadRent = fields.Integer(default=3500)
    tenantRef_ids = fields.One2many('acom.tenant.model','roomRef_id')
    property_id = fields.Many2one('acom.property.model')
    tenantLen = fields.Integer()
    uniqueRoomNum = []

    # _sql_constraints=[
    #     ('unique_roomNumber','unique(roomNumber)','error')
    #     ]

    @api.depends("tenantRef_ids")
    def _compute_current_cap(self):
        for record in self:
            record.currentCap = len(record.tenantRef_ids)
            record.tenantLen = len(record.tenantRef_ids)
            if(record.tenantLen>record.maxCap):
                raise exceptions.UserError("Maximum tenants per room can only be %d" %record.maxCap)

    @api.depends("property_id.propEachRoomSharing")
    def _compute_max_cap(self):
        for record in self:
            record.maxCap = record.property_id.propEachRoomSharing

    # @api.model
    # def create(self,vals):
    #     # prop = self.env['acom.rooms.model'].browse(vals['roomNumber'])
    #     if(vals['roomNumber'] in self.uniqueRoomNum):
    #         raise exceptions.UserError("Room number should be unique")
    #     else:
    #         self.uniqueRoomNum.append(vals['roomNumber'])
    #     return super(AcomRoomsModel,self).create(vals)

    # @api.ondelete(at_uninstall=False)
    # def _unlink_if_deleted(self,vals_list):
    #     for record in self.uniqueRoomNum:
    #         if(record not in self.mapped('roomNumber')):
    #             self.uniqueRoomNum.remove(record)
    #     # if(vals['roomNumber'] not in self.uniqueRoomNum):
    #     #     self.uniqueRoomNum.remove(vals['roomNumber'])
    #         return super().create(vals_list)
