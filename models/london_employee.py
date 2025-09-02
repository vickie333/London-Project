from odoo import fields, models, api
from odoo.exceptions import ValidationError

class LondonEmployee(models.Model):
    _name = 'london.employee'


    name = fields.Char(string='Name', required=True)
    role = fields.Selection([
        ('pm', 'Project Manager'),
        ('dev', 'Dev'),
    ], string='Role', required=True, default='dev')

    project_id = fields.Many2one('london.project', string='Assigned Project')
    project_manager_id = fields.Many2one('london.employee', string='Project Manager')
    color = fields.Integer(compute='_get_color', store=True)
    
    # Nuevo campo de estado de asignación
    assignment_status = fields.Selection([
        ('available', 'Disponible'),
        ('assigned', 'Asignado a Proyecto'),
        ('overloaded', 'Sobrecargado'),
    ], string='Estado de Asignación', compute='_compute_assignment_status', store=True)

    @api.constrains('project_manager_id', 'role')
    def _check_manager_role(self):
        for rec in self:
            # Un PM no puede tener manager asignado
            if rec.role == 'pm' and rec.project_manager_id:
                raise ValidationError("Un Project Manager no puede tener otro Project Manager asignado.")
            
            # Si se asigna un manager, debe ser PM
            if rec.project_manager_id and rec.project_manager_id.role != 'pm':
                raise ValidationError("El manager asignado debe tener rol 'Project Manager'.")

    @api.depends('role')
    def _get_color(self):
        """Compute Color value according to the conditions"""
        for rec in self:
            if rec.role == 'pm':
                rec.color = 1
            else:
                rec.color = 2

    @api.depends('project_id', 'role')
    def _compute_assignment_status(self):
        """Compute assignment status based on project assignment and role"""
        for rec in self:
            if not rec.project_id:
                rec.assignment_status = 'available'
            elif rec.role == 'pm':
                # Los PM pueden estar en múltiples proyectos, considerarlos sobrecargados si tienen muchos
                project_count = self.search_count([('project_manager_id', '=', rec.id)])
                if project_count > 2:
                    rec.assignment_status = 'overloaded'
                else:
                    rec.assignment_status = 'assigned'
            else:
                # Los devs normalmente están en un proyecto
                rec.assignment_status = 'assigned'

