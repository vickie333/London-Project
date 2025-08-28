# models/import_employee_wizard.py
from odoo import models, fields
import base64
import openpyxl
from io import BytesIO
from odoo.exceptions import UserError

class ImportEmployeeWizard(models.TransientModel):
    _name = 'import.employee.wizard'
    _description = 'Importar Empleados desde Excel'

    file = fields.Binary('Archivo Excel (.xlsx)', required=True)
    file_name = fields.Char('Nombre del archivo')

    def action_import_file(self):
        if not self.file:
            raise UserError("Por favor, sube un archivo.")
        data = base64.b64decode(self.file)
        try:
            wb = openpyxl.load_workbook(filename=BytesIO(data), read_only=True)
            ws = wb.active
        except Exception as e:
            raise UserError(f"Error al leer el archivo: {e}")

        for idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            name, role, manager_name = row[:3]  # ajusta según columnas
            if not name:
                continue
            vals = {
                'name': name,
                'role': role,
            }
            if manager_name:
                manager = self.env['employee.london'].search([('name', '=', manager_name)], limit=1)
                if manager:
                    vals['project_manager_id'] = manager.id
            self.env['employee.london'].create(vals)
        return {'type': 'ir.actions.act_window_close'}
