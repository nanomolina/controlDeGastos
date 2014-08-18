controlDeGastos
===============

Este es un pequeño programa con interfaz gráfica escrito en python para el control de gastos. 
Este proyecto empezó con el motivo de que llegaba fin de mes y nunca sabia en que se me había ido la plata.
Por este motivo lo desarrollé con el propósito de mantenerme al tanto de todos mis gastos. :)

El programa funciona mediante una base de datos que es proporcionada por una libreria de python (sqlite3),
en la cual irémos almacenando los datos de las varias tablas.

Fue diseñado de tal forma de que se lleve una cuenta por cada mes/año con la opción de insertar el presupuesto 
incial que tendremos disponible durante todo el mes.

La insersión de datos a la tabla de datos es de 4 tipos: Producto, Precio, Fecha y Comprador.


Plataformas
-----------
  
  * Debian, Ubuntu

Dependencias
------------

  * PyQT4
  * sqlite3

Ejecutar programa
-----------------

  * Para descargar el fichero necesitaremos el sistema de control [git](http://git-scm.com/ "git").
    - sudo apt-get install git 

  * Luego de haber instalado git, mediante terminal ejecutamos la siguiente instrucción para descargar el fichero.
    El fichero se descargará en el directorio actual en el que nos encontremos.
    - git clone https://github.com/nanomolina/controlDeGastos.git

  * La dependencia Pyqt4 puede descargarse desde el siguiente link:
    - http://www.riverbankcomputing.co.uk/software/pyqt/download

  * La Dependencia sqlite se instala ejecutando el siguiente código:
    - sudo apt-get install sqlite3

  * Luego que ya hemos instalado todo, para ejecutar el programa podemos utilizar cualquiera de estas dos formas:
    - python app.py
    - ./app.py
