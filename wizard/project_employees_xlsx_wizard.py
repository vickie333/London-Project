# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import io
import base64
import xlsxwriter
from odoo.exceptions import UserError

class ProjectEmployeesXlsxWizard(models.TransientModel):
    _name = 'project.employees.xlsx.wizard'
    _description = 'Exportar empleados por proyecto a XLSX (sencillo)'

    project_ids = fields.Many2many('london.project', string='Proyectos',
                                   help='Si no seleccionas ninguno se exportan todos los proyectos.')
    file_name = fields.Char(string='Nombre de archivo')
    file_data = fields.Binary(string='Archivo (.xlsx)', filename='file_name')

    def _get_projects(self):
        if self.project_ids:
            return self.project_ids
        return self.env['london.project'].search([])

    def action_generate_xlsx(self):
        """Genera el XLSX, lo guarda en file_data y reabre el wizard para descargar."""
        projects = self._get_projects()
        if not projects:
            raise UserError(_("No se encontraron proyectos para exportar."))

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        header_fmt = workbook.add_format({'bold': True})

        for proj in projects:
            sheet_name = (proj.name or 'Proyecto')[:31]
            worksheet = workbook.add_worksheet(sheet_name)
            worksheet.write(0, 0, 'Empleado', header_fmt)
            worksheet.write(0, 1, 'Rol', header_fmt)
            row = 1
            for emp in proj.employee_ids:
                worksheet.write(row, 0, emp.name or '')
                role_label = ''
                try:
                    role_field = emp._fields.get('role')
                    if role_field and getattr(emp, 'role', False):
                        role_label = dict(role_field.selection).get(emp.role, emp.role)
                except Exception:
                    role_label = emp.role or ''
                worksheet.write(row, 1, role_label)
                row += 1
            if row == 1:
                worksheet.write(1, 0, '--- Sin empleados asignados ---')
            worksheet.set_column(0, 0, 30)
            worksheet.set_column(1, 1, 20)

        workbook.close()
        output.seek(0)
        data = output.read()
        filename = 'Proyectos_Empleados.xlsx'
        self.write({
            'file_name': filename,
            'file_data': base64.b64encode(data),
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'project.employees.xlsx.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }
