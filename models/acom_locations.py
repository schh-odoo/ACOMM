from odoo import fields,models,api,exceptions

class AcomLocationsModel(models.Model):
    _name="acom.locations"
    _description="property locations"
    _rec_name="acom_locations"

    acom_locations = fields.Char(string="Location")
