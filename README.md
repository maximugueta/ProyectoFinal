#Proyecto Diario

Alumnos: Matias Lopez Touzon
         Maximiliano Mugueta
         
Creamos una web pensada en función de un diario donde habrán diferentes secciones para notas, y con diferentes tipos de usuarios.
Para esta entrega, se establecieron 3 clases: usuarios, colaboradores, staff.

Una vez que se corra el server, ingresaremos a http://127.0.0.1:8000/AppDiario/ la cual será nuestra página de inicio.
Dentro del inicio veremos los links correspondientes a las páginas de Usuarios, Colaboradores y Staff

En la sección usuarios, encontraremos el formulario de carga de datos para un alta de los usuarios de la web:
/AppDiario/usuarios/
Datos a ingresar: Nombre, Email, Edad, País

En la sección colaboradores, se encuentra el formulario con carga de datos para un alta de los colaboradores de la web:
/AppDiario/colaboradores/
Datos a ingresar: Nombre, Email, Edad, Especialidad

Por último, en la sección Staff, se ve el formulario para carga de datos para un alta del staff de la web:
/AppDiario/staff/
Datos a ingresar: Nombre, Email, Edad, Categoría.

Para realizar las búsquedas de las entradas en la DB, disponemos de tres url:
http://127.0.0.1:8000/AppDiario/busquedaUsuario/
http://127.0.0.1:8000/AppDiario/busquedaColaborador/
http://127.0.0.1:8000/AppDiario/busquedaStaff/

También disponemos de un superusuario Admin para poder ingresar a ver los datos desde
http://127.0.0.1:8000/admin/

usuario: admin
password: admin