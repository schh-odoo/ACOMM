from odoo import models,fields,api,exceptions

class AcomPropertyModel(models.Model):
    _name="acom.property.model"
    _description="Table to hold property information"
    _sql_constraints=[
        ('unique_prop_name','unique(name)','Property name should be unique')
        ]

    name = fields.Char(required=True)
    propImg = fields.Image(string="Brand Image", max_width=150, max_height=150)
    propManager_id=fields.Many2one('res.users', string='Manager', index=True)
    propAddress = fields.Char(required=True, string="Address")
    propLocation_id = fields.Many2one("acom.locations",required=True,string="Location")
    propPostcode = fields.Integer(required=True, string="Postcode")
    propOccupancy = fields.Integer(string="Occupied", readonly=True,compute="_compute_occupancy")
    state = fields.Selection(
        string="Status",
        selection=[('underconstruction', 'Under Construction'), ('active', 'Active'),('underrennovation', 'Under Rennovation'), ('renovated', 'Rennovated')],
        default="active",
        required=True,
        copy=False
    )
    totalOccupancy = fields.Integer(string="Total Occupancy",readonly=True,compute="_compute_total_occupancy")
    propRentalIncome = fields.Integer(string="Rental Income", readonly=True,compute="_compute_rental_income")
    propRoomsNumber = fields.Integer(string="No. of Rooms")
    propFloors = fields.Integer(string="No. of Floors")
    propFor = fields.Selection(string='For',
        selection=[('boys', 'Boys'), ('girls', 'Girls')],
        help="Boys/Girls Only")
    active = fields.Boolean(default = True, string="Active")
    propEachRoomSharing = fields.Integer()
    propRooms_ids = fields.One2many('acom.rooms.model','property_id')
    propTenatAllocation_ids = fields.One2many('acom.tenant.model','propAllocated_id')
    roomLen = fields.Integer()
    color = fields.Integer(compute="_compute_color",default=4)
    is_favorite = fields.Boolean(default=False,string="Favorite")

    @api.depends("propFor")
    def _compute_color(self):
        for record in self:
            if(record.propFor=="boys"):
                record.color = 9
            elif(record.propFor=="girls"):
                record.color = 10
            else:
                record.color = 1

    @api.depends("propRooms_ids")
    def _compute_occupancy(self):
        for record in self:
            record.propOccupancy = sum(record.propRooms_ids.mapped("currentCap"))
            record.roomLen = len(record.propRooms_ids)
            if(record.roomLen>record.propRoomsNumber):
                raise exceptions.UserError("Rooms cannot be more than %d" %record.propRoomsNumber)

    @api.depends("propRoomsNumber","propEachRoomSharing")
    def _compute_total_occupancy(self):
        for record in self:
            record.totalOccupancy = (record.propRoomsNumber*record.propEachRoomSharing)

    @api.depends("propRooms_ids.tenantRef_ids")
    def _compute_rental_income(self):
        for record in self:
            record.propRentalIncome = sum(record.propRooms_ids.tenantRef_ids.mapped("rent"))
