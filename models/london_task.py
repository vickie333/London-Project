from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LondonTask(models.Model):
    _name = 'london.task'
    _description = 'Tarea del proyecto'

    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    project_id = fields.Many2one('london.project', string='Proyecto', required=True)
    assigned_to_id = fields.Many2one('london.employee', string='Asignado a:')


    @api.onchange('project_id')
    def _onchange_project_id(self):
        if self.project_id:
            assigned_employees = self.project_id.assign_dev_ids.ids
            return {'domain': {'assigned_to_id': [('id', 'in', assigned_employees)]}}
        return {'domain': {'assigned_to_id': []}}