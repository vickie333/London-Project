from odoo import fields, models, api
from odoo.exceptions import ValidationError

class EmployeeLondon(models.Model):
    _name = 'employee.london'


    name = fields.Char(string='Name', required=True)
    role = fields.Selection([
        ('pm', 'Project Manager'),
        ('dev', 'Dev'),
    ], string='Role', required=True, default='dev')

    project_id = fields.Many2one('london.project', string='Assigned Project')
    project_manager_id = fields.Many2one('employee.london', string='Project Manager')

    @api.constrains('project_manager_id')
    def _check_manager_role(self):
        for rec in self:
            if rec.project_manager_id and rec.project_manager_id.role != 'pm':
                raise ValidationError("El manager asignado debe tener rol 'Project Manager'.")

