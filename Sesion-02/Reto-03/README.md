## `RETO 3`




</br>


![Alt text](../Reto-03/assets/github.png?raw=true "DevOps")


</br> 


**`Completa el siguiente Reto: `**


</br>



***1. Crear un repositorio nuevo en github***
</br>
Incluyendo su Readme.

</br>

***2. Ahora crea en Actions un nuevo workflow de tipo Python***
</br>
Creando el siguiente archivo con el siguiente contenido.


*pythonapp.yml
</br>


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

***3. Agrega la siguiente estructura de archivos y directorios en tu Repositorio.***
</br>
 
</br>

~~~
└── python
    ├── Dockerfile
    ├── app.py
    └── requirements.txt
 
~~~
</br>

Dockerfile:


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
Flask==1.0.2
~~~
</br>


***4. Asegurate de subir los cambios al repositorio.***

</br>

***5. Crea un nuevo***
**` Branch `**


</br>

***6. Edita  el archivo app.py en la linea*** **`print`**

</br>

***7. Sube este ultimo cambio a tu***
**`Branch`**

</br>

***8. Regresa **` GitHub`** y crea un***
**` Pull Request`**

</br>

***9. Muevete a **` Action `**
, y si todo salio bien  veras  tu***
**` Workflow `**

</br>

***10. Regresa a tu 
**` Pull Request `**
 y ya podras fucionarlo*** **` (Merged) `**

</br>

***11. No olvides eliminar tu***
**` Branch  `**
</br>