
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
        'views/wizard_views.xml',
        'views/project_date_range_wizard.xml',
        'views/project_views.xml',
        'views/import_wizard.xml',
        'views/emp_views.xml',
        'views/menu_views.xml',
    ],
}
