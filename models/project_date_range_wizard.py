from odoo import models, fields, _
from odoo.exceptions import UserError

class ProjectDateRangeWizard(models.TransientModel):
    _name = 'project.date.range.wizard'
    _description = 'Wizard: Proyectos que terminan en un rango de fecha'

    date_from = fields.Date(string='Fecha desde', required=True, default=fields.Date.today)
    date_to = fields.Date(string='Fecha hasta', required=True, default=fields.Date.today)

    def action_open_projects(self):
        self.ensure_one()
        if self.date_from > self.date_to:
            raise UserError(_("La fecha inicial no puede ser mayor que la final."))

        action = self.env.ref('london_project.action_london_project').read()[0]
        action['domain'] = [
            ('date_end', '>=', self.date_from),
            ('date_end', '<=', self.date_to),
        ]
        # Opcional: título dinámico
        action['name'] = _("Proyectos que terminan entre %s y %s") % (self.date_from, self.date_to)
        return action