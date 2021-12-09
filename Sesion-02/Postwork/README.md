

### POSTWORK ###
---

</br>

**`Sesión 02`**


</br>

# Creación de código en distintas ramas y fusión entre ellas. #

</br>

🎯 Objetivo

</br>

Crear un repositorio con distintos branchs.
Modificar el código principal en distintas ramas.
Subir archivos y directorios a Master/Main.

</br>


Antes de empezar

</br>

🧑‍💻 Nota de expert@ 

En esta sección encontrarás algunos tips por si algún recurso mostrado viene en otro idioma y encontrarás la instalación necesaria para tu módulo.

</br>

Algunos recursos están en inglés. Si prefieres leerlos en español, puedes hacer de Google tu traductor predeterminado, quien te ofrecerá la opción de traducir la página que vas a consultar. 


</br>

Otra opción es usar un traductor desde cualquier buscador.  


</br>

## ⚙️ Setup ##

</br>

### Editor de código. ###

* Visual Studio Code 

</br>

### Versionamiento de código. ###
* Git 
* Tener una cuenta de GitHub

</br>


  # Desarrollo 🚀

</br>

## Descripción: ##
</br>

En este PostWork vas a trabajar con 3 desarrolladores, cada uno con una copia de Master/Main, o sea, cada quien hará una rama directa de la rama principal, toma en cuenta los siguientes pasos:

1. Crea un repo en **`github.com`**

</br>


![Alt text](..//Postwork/assets/1.png?raw=true "DevOps")



</br>

* Coloca un nombre como: **`DevOpsBeduReto02`**

</br>


![Alt text](..//Postwork/assets/2.png?raw=true "DevOps")

</br>

**` Nota: `** Al reto deberás añadirle el **`README.md`**

</br>


![Alt text](..//Postwork/assets/2.1.png?raw=true "DevOps")

</br>


3. Clona el **`branch `** en tu local, como se muestra en la imagen:



</br>

![Alt text](..//Postwork/assets/s2-e02-04.png?raw=true "DevOps")

</br>

4. Puede ser directo en el cliente de **`GitHub Desktop.`**


![Alt text](..//Postwork/assets/s2-e02-05.png?raw=true "DevOps")

</br>

5. Pega la dirección en el apartado : **`URL`**

![Alt text](..//Postwork/assets/s2-e02-06.png?raw=true "DevOps")

</br>

6. Abre el nuevo Repositorio con el editor de texto.


![Alt text](..//Postwork/assets/s2-e02-07.png?raw=true "DevOps")


7. Vas a crear la siguiente estructura de archivos y directorios, en **`Master/Main:`**
</br>

~~~
.
├── README.md
└── python
    └── aplicacion.py

~~~
</br>






Donde el contenido de **`aplicacion.py `** tendra la siguientes lineas:


</br>

~~~

def main():
  # Imprimir en pantalla mensaje.
  print("Hola Bedu! Esto Es Codigo de la Rama Principal!")
# Llamando a funcion principal.
main()

~~~
</br>



8. Prepara el Commit para subirlo a **`Master/Main.`**

</br>

![Alt text](..//Postwork/assets/s2-e02-11.png?raw=true "DevOps")

</br>

9. Recuerda el Objetivo: **`Tienes 3 desarrolladores`**
, donde cada desarrollador estará trabajando en una característica
**`(Feature)`** nueva de tu aplicación. Ya que tienes desarrollado tu plan de trabajo, vas a crear los **`branchs`** en el cliente de **`GitHub:`**


</br>

10. Cada desarrollador deberá estar trabajando en su propia rama **`(branch)`**. Quedando de la siguiente manera:

</br>

## Desarrollador 1: ##


#### Característica:  Botón de Inicio

#### Rama: feature/botonIniciar

</br>


![Alt text](..//Postwork/assets/s2-e02-08.png?raw=true "DevOps")



</br>


## Desarrollador 2: ##

</br>

#### Característica: Botón de Detener

#### Rama: feature/botonDetener


</br>

![Alt text](..//Postwork/assets/s2-e02-09.png?raw=true "DevOps")


</br>


## Desarrollador 3: ##

</br>

#### Característica: Botón de Siguiente
#### Rama: feature/botonSiguiente

</br>


![Alt text](..//Postwork/assets/s2-e02-10.png?raw=true "DevOps")

</br>

11. Ahora, cada desarrollador tiene una copia en la rama principal en su local, y puedes comenzar a codificar sin interferir en los cambios de los demás.

</br>

12. Dentro del directorio **`python`** crea una clase nueva por rama, o sea, cada desarrollador subirá una clase distinta:


</br>

## Desarrollador 1: ##

</br>

Archivo:
</br>
**`aplicacionDev01.py`**


</br>


~~~
def main():
  # Imprimir en pantalla mensaje.
  print("Hola Bedu! Esto Es Codigo del Desarrollador 1")
# Llamando a funcion principal.
main()
~~~
</br>


Quedando de la siguiente manera:

![Alt text](..//Postwork/assets/s2-e02-11.png?raw=true "DevOps")

</br>

Sube el cambio a la rama principal.


![Alt text](..//Postwork/assets/s2-e02-12.png?raw=true "DevOps")

</br>


Ahora, deberás crear tu **`Pull Request `** como se muestra a continuación:

</br>

![Alt text](..//Postwork/assets/s2-e02-13.png?raw=true "DevOps")

</br>

Dirígete a GitHub.com para finalizar el **`Pull Request (PR):`**

</br>


![Alt text](..//Postwork/assets/s2-e02-14.png?raw=true "DevOps")

</br>

De la siguiente forma verás tu **`PR`**
 en espera de ser fusionado **`(Merged)`**

 </br>


![Alt text](..//Postwork/assets/s2-e02-15.png?raw=true "DevOps")

</br>

Te solicitará confirmación para realizar la fusion **`(Merged)`**


</br>


![Alt text](..//Postwork/assets/s2-e02-16.png?raw=true "DevOps")

</br>

## Nota: Se recomienda la eliminación de la rama  ###     
**`(branch)`**

</br>

![Alt text](..//Postwork/assets/s2-e02-17.png?raw=true "DevOps")

</br>

13. Importante:
**`Repite los pasos del punto 12`**
, únicamente creando los archivos correspondientes por desarrollador, quedando de la siguiente manera:

</br>

## Desarrollador 2: ##

</br>

Archivo:

**` aplicacionDev02.py `**


</br>

~~~
def main():
  # Imprimir en pantalla mensaje.
  print("Hola Bedu! Esto Es Codigo del Desarrollador 2")
# Llamando a funcion principal.
main()
~~~

</br>


### Desarrollador 3: ###

</br>

Archivo:

**`aplicacionDev03.py`**

</br>

~~~

def main():
  # Imprimir en pantalla mensaje.
  print("Hola Bedu! Esto Es Codigo del Desarrollador 3")
# Llamando a funcion principal.
main()

~~~
</br>


14. Si todo ha salido de forma correcta, ahora debemos tener 3 nuevos archivos **` Python `** en nuestra rama **`Master/Main.`**


Solo resta traer los cambios al local, quedando de la siguiente manera:

</br>


![Alt text](..//Postwork/assets/s2-e02-29.png?raw=true "DevOps")





 ¡Felicidades!, has concluido el PostWork.😃


## ¡Recapitulemos! ##

* Deberás crear un repositorio con distintos branchs.
* Modificar el código principal en distintas ramas.
* Clonar un branch.
* Estructurar archivos y directorios
* Subir archivos y directorios a Master/Main.
* Crear un  branchs en  GitHub.


</br>

✅ CHECKLIST 

Considera que tu proyecto debe cumplir con lo siguiente:



![Alt text](..//Postwork/assets/lista.png?raw=true "DevOps") 


