# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LondonProject(models.Model):
    _name = 'london.project'
    _description = 'London Project'

    name = fields.Char(required=True)
    client_id = fields.Many2one('res.partner',string="Client", required=True)
    client_is_company = fields.Boolean(related='client_id.is_company',string='Cliente es empresa')
    client_object = fields.Char(string='Objeto social') 
    date_start = fields.Date()
    date_end = fields.Date()
    manager_id = fields.Many2one('employee.london', string='Project Manager')
    employee_ids = fields.One2many('employee.london', 'project_id', string='Participantes')
    task_ids = fields.One2many('london.task', 'project_id', string='Lista de Tareas')

    assign_dev_ids = fields.Many2many(
        'employee.london',
        string='Equipo (seleccionar devs)',
        compute='_compute_assign_dev_ids',
        inverse='_inverse_assign_dev_ids',
        store=False, 
    )

    @api.constrains('manager_id')
    def _check_manager_role(self):
        for rec in self:
            if rec.manager_id and rec.manager_id.role != 'pm':
                raise ValidationError("El jefe de proyecto debe tener el rol 'Project Manager'.")

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for rec in self:
            if rec.date_start > rec.date_end:
                raise ValidationError("La fecha de inicio debe ser anterior a la de finalización.")

    @api.depends('employee_ids')
    def _compute_assign_dev_ids(self):
        for rec in self:
            rec.assign_dev_ids = rec.employee_ids

    def _inverse_assign_dev_ids(self):
        for rec in self:
            current = rec.employee_ids
            new = rec.assign_dev_ids
            to_add = new - current
            to_remove = current - new

            if to_add:
                to_add.write({
                    'project_id': rec.id,
                    'project_manager_id': rec.manager_id.id if rec.manager_id else False,
                })

            if to_remove:
                to_remove.write({'project_id': False})
    