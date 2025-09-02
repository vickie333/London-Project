
{
    'name': "London Project",
    'summary': "Gestión de proyectos, empleados y reportes",
    'description': """
                Módulo para la gestión de proyectos, empleados y generación de reportes en Odoo.
                """,
    'version': '0.1',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/project_employees_xlsx_wizard_views.xml',
        'wizard/project_date_range_wizard_views.xml',
        'wizard/import_employee_wizard_views.xml',
        'views/london_project_views.xml',
        'views/london_employee_views.xml',
        'views/london_employee_menu_views.xml',
    ],
}
