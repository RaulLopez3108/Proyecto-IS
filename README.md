# LIBRERIA BÚHO 🦉🕮

## Descripción del proyecto:
Librería Búho: es una aplicación de escritorio desarrollada con el framework Flet en Python. Está diseñada para facilitar el acceso y la gestión de libros de las bibliotecas de la Universidad de Sonora.
Los alumnos podrán consultar fácilmente la disponibilidad de libros de su interés 

## 1 INTRODUCCION
 ### 1.1 Proposito
 Este documento describe el diseño,funcionalidades y estructura del sistema de una libreria,permitiendo a los usuarios buscar libros
 ### 1.2 Alcance
Este sistema permite :
a los administradores
+ Agregar libros
+ Eliminar libros 
+ Ver la lista de usuarios
+ ver la lista de libros
a los usuarios: 
+ Registrarse 
+ buscar libros

## 2 Arquitectura del sistema 

### 2.1 Diagrama General
- diagramas de entidad relacion y casos de uso

### 2.2 Tecnologias utilizadas
+ Backend: Python 
+ Frontend: Flet
+ Base de datos: MySQL

### 3 Metodologia
La aplicacion se desarrollo mediante la metodologia agil SCRUM, el cual se dividio en las siguientes fases 
+ Fase 1:
    Planificación del proyecto:
    Discusiones sobre que tipo de aplicacion queriamos hacer,
    que deberia hacer el sistema

    Arquitectura del sistema:
    Seleccionamos el framework Flet de python para hacer nuestro sistema ya que funciona tanto para aplicaciones de escritorio como paginas web, y decidimos usar MySQL para nuestra base de datos 

    Planificacion del proyecto:
    Usamos JIRA para poder definir bien las tareas a realizar y repartirlas y definimos las responsabilidades de cada miembro del equipo

+ Fase 2: Interfaz de usaurio (frontend)
    Definimos como se veria el sistema, queriamos que fuera facil de usar 

+ Fase 3: Desarrollo (backend, base de datos,consultas a la base de datos)
    Empezamos haciendo el login y el registro de nuevos usuarios, verificamos que los usuarios nuevos se vean reflejados en la base de datos, a partir de tener el login desarrollamos las funciones de agregar, eliminar y buscar un libro, despues las funciones para ver la lista de usuarios 



## Miembros del equipo: 
+ Raul Leonardo Lopez Ruiz
+ Gabriela Aydee Miranda
+ Gael Juan Valenzuela
+ Jesus Alberto Paredes Barnett
+ Jesus Flores Lacarra

## Ficha técnica de la aplicación
+ Nombre: Librería Búho
+ Framework: Flet (python)
+ Tipo de app: Escritorio
+ Funcionalidades: inicio de sesión, registro de usuarios, validacion, panel de usuario y administrativo
+ Validacion: formato de correo, contraseña
+ Usuarios: Estudiantes(acceso general) y Administradores(acceso especial)

  
