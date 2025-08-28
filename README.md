# London Project Management System

## Descripción

El **London Project Management System** es un módulo desarrollado para **Odoo 18** destinado a la gestión integral de proyectos y empleados en la empresa **Londres S.A**. Este sistema permite controlar proyectos, roles de empleados y reportes consolidados de forma eficiente.

Con este módulo podrás:

- Gestionar proyectos, incluyendo fechas de inicio y fin, descripción, tareas y empleados participantes.
- Controlar empleados y sus roles dentro de la empresa.
- Asignar empleados a jefes de proyecto y garantizar que cada empleado tenga un único jefe.
- Asociar proyectos a clientes y registrar información relevante sobre ellos.
- Generar reportes en Excel por proyecto con los empleados y sus roles.
- Importar de manera masiva empleados mediante archivos Excel.

---

## Funcionalidades

### Gestión de Empleados

- Registro de empleados con su **rol** (Jefe de Proyecto o Desarrollador).
- Los **jefes de proyecto** pueden controlar un grupo de empleados.
- Cada empleado está asignado a un único jefe de proyecto.
- Los desarrolladores solo pueden trabajar en un proyecto a la vez.

### Gestión de Proyectos

- Cada proyecto tiene:
  - **Jefe de proyecto**
  - **Fecha de inicio y fin**
  - **Descripción general**
  - **Lista de tareas**
  - **Empleados participantes**
- Cada proyecto está asociado a un **cliente**:
  - Persona natural o empresa
  - En caso de empresa, se registra el **objeto social**

### Reportes

- Generación de **Excel** con pestañas por proyecto.
- Cada pestaña muestra los empleados asignados y sus roles.

### Importación Masiva

- Permite cargar empleados de manera masiva desde un archivo Excel.

---

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/vickie333/London-Project.git
