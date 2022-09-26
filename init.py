from odoo import fields, models, api
#cambios

class ResPartner(models.Model):
    _inherit = "res.partner"

    def _get_invoice_lines(self):
        return self.mapped("invoice_line_ids")

