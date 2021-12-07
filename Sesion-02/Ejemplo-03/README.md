## Trunk-based development ##


**`Objetivo:`**



1.Crear nuevo repositorio en GitHub.com

2. Creación del primer Workflow

3. Commit de nuestra primera aplicación.

4. Generación de una nueva Rama 

5. Compilación y validación de nuestro código

6. Fusionar nuestros cambios con la Rama principal.


</br>

**`Desarrollo:`**

</br>

Crear nuevo repositorio en: 

</br>

~~~

https://github.com/new
~~~
</br>  

![Alt text](../Ejemplo-03/assets/s2-e03-01.png?raw=true "DevOps")



</br>

Nombre del Repo:
</br>

~~~
DevOpsSesion03-Ejemplo03
~~~
</br>

Descripción:

</br>

~~~
Ejemplo 03 Trunk-based development
~~~
</br>

Tipo de visibilidad del repo:

**Publico**
</br>

Agregar archivo inicial README.md
</br>

~~~
Add a README file
~~~
</br>

![Alt text](../Ejemplo-03/assets/s2-e03-02.png?raw=true "DevOps")

</br>

Tenemos nuevo repositorio, creado directo en github.com

![Alt text](../Ejemplo-03/assets/s2-e03-03.png?raw=true "DevOps")



Buscamos la opción Actions:

![Alt text](../Ejemplo-03/assets/s2-e03-04.png?raw=true "DevOps")




Ahora buscamos Python package:

![Alt text](../Ejemplo-03/assets/s2-e03-05.png?raw=true "DevOps")



Nuevo archivo:

</br>

~~~
DevOpsSesion03-Ejemplo03/.github/workflows/pythonapp.yml
~~~
</br>

Contenido de nuestro pythonapp.yml

</br>

~~~
name: Python application

on:
  pull_request:
    paths:
    - 'python/*'
      
jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v1
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r ./python/requirements.txt
        python3 ./python/app.py
~~~

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-06.png?raw=true "DevOps")


Procedemos a dar commit:


![Alt text](../Ejemplo-03/assets/s2-e03-07.png?raw=true "DevOps")

</br>

Podemos ver el archivo de nuestro workflow creado:

![Alt text](../Ejemplo-03/assets/s2-e03-08.png?raw=true "DevOps")


GitHub Desktop en accion:

Ya debemos tener nuestro cliente de GitHub instalado en nuestro local:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-09.png?raw=true "DevOps")

</br>

Vamos a clonar nuestro repositorio:

</br>


![Alt text](../Ejemplo-03/assets/s2-e03-10.png?raw=true "DevOps")

</br>


Debemos copiar la URL desde el sitio de nuestro repo de github.com

</br>


![Alt text](../Ejemplo-03/assets/s2-e03-11.png?raw=true "DevOps")

</br>

Ahora, la colocamos en la pestaña de URL de nuestro cliente GitHub:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-12.png?raw=true "DevOps")


</br>

Siguiente, buscamos la opción de Abrir nuestro repositorio en nuestro editor de texto:

</br>


![Alt text](../Ejemplo-03/assets/s2-e03-13.png?raw=true "DevOps")


</br>

A continuación vamos a crear tres archivos para nuestro ejemplo, quedando con una apariencia similar:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-14.png?raw=true "DevOps")

</br>
Estructura de archivo:

</br>

~~~

└── python
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
~~~
</br>

Dockerfile
</br>

~~~
FROM python:3-alpine
COPY . /python
WORKDIR /python
RUN pip install -r requirements.txt
CMD python /python/app.py

~~~
</br>

app.py
</br>

~~~

def main():
   # Print a single text
   print("Hola Bedu!")
 
# Call the main function.
main()

~~~
</br>

requirements.txt

</br>

~~~
</br>
Flask==1.0.2

~~~
</br>

En nuestro cliente de GitHub veremos algo similar, escribimos un comentario acerca de nuestros cambios, seguido de Commit to main

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-15.png?raw=true "DevOps")

</br>

Empujamos nuestros cambios a la rama principal (main)

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-16.png?raw=true "DevOps")

</br>

En github.com podremos ver nuestro archivo actualizado, junto con el comentario:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-17.png?raw=true "DevOps")


</br>

Regresamos a Actions dentro de github.com, podremos ver la ejecución de nuestro primer workflow.

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-18.png?raw=true "DevOps")


</br>

De nuevo, en nuestro cliente de GitHub crearemos una nueva rama, llamada feature/updateApp:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-19.png?raw=true "DevOps")

</br>

Vamos a actualizar nuestro print en nuestro python:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-20.png?raw=true "DevOps")

</br>

Subimos nuestros cambios a nuestra rama:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-21.png?raw=true "DevOps")

</br>

Volvemos a Actions en GitHub y prestamos atencion a la ejecucion del workflow:


![Alt text](../Ejemplo-03/assets/s2-e03-22.png?raw=true "DevOps")

</br>

Logramos ver los cambios en nuestro log:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-23.png?raw=true "DevOps")

</br>


Nuestro Pull Request ha compilado de forma satisfactoria, por lo tal, podemos fusionar (merged) a nuestra rama principal:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-24.png?raw=true "DevOps")

</br>


Por último, se recomienda eliminar ramas que ya hayan sido unificadas:

</br>

![Alt text](../Ejemplo-03/assets/s2-e03-25.png?raw=true "DevOps")
