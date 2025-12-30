# Tareas_DWES

Aplicación web desarrollada con **Django** para la gestión de tareas en un centro educativo.

La aplicación permite gestionar tareas tanto para **alumnos** como para **profesores**, con control de roles, validación de tareas y distintos tipos de asignaciones.

## Estado del proyecto
En desarrollo


## Tecnologías utilizadas
- Python 3.x
- Django 4.x
- PostgreSql



## Descripción general

La aplicación permite:
- Gestión de usuarios con roles (alumno / profesor)
- Creación de tareas individuales y grupales
- Validación de tareas por parte de profesores
- Asignación de tareas a uno o varios alumnos
- Control de estados y fechas importantes


## Modelo de datos

### Usuario (hereda de 'AbstractUser')

* [x] Identificador id (automático)
* [x] username
* [x] first_name
* [x] last_name
* [x] email
* [x] password
* [x] rol (alumno/profesor)
* [x] fecha de alta (automática)
* [x] ultima conexión (automática)


Las tareas se crearán mediante un formulario y necesitarán, o no, ser validadas por un profesor.

### Tarea
* [x] Identicador uuid (automático)
* [x] titulo
* [x] descripción
* [x] fecha_creación
* [x] fecha_recordatorio
* [x] creador
* [x] estado
* [x] requiere_validación
* [x] profesor


### Tipos de tareas
Existirán dos tipos de tareas, individuales o grupales, que heredarán de la clase principal 'Tarea'.

#### TareaIndividual
* [x] alumno

#### TareaGrupal
* [x] alumnos



## Roles y permisos

**Alumno** 
    [x] Puede crear y consultar tareas
    [x] Puede completar tareas asignadas

**Profesor**
    [x] Puede crear tareas
    [x] Puede validar tareas
    [x] Puede asignar tareas a uno o más alumnos


## Vistas

### Vistas basadas en clases (CBV)
- [x] Detalle de tarea
- [x] Registro de usuarios
- [x] Creación de tareas individuales
- [x] Creación de tareas grupales



### Vistas basadas en funciones (FBV)
- [x] Perfil de usuario
- [x] Listado de usuarios
- [x] Listado de tareas del usuario
- [x] Listado de tareas pendientes de validación



## Formularios
- [x] Registro de usuarios con validación de contraseña
- [x] Creación de tareas individuales
- [x] Creación de tareas grupales
- [x] Filtrado de usuarios por rol (alumno / profesor)



## URLs
- [x] `/registro/`
- [x] `/crear_tarea_individual/`
- [x] `/crear_tarea_grupal/`
- [x] `/<uuid>/`
- [x] `/perfil/<id>/`
- [x] `/lista_usuarios/`
- [x] `/lista_tareas_usuario/<id>/`
- [x] `/lista_tareas_validacion/<id>/`