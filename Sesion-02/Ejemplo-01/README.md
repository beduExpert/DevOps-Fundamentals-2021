#  Creación/Clonación de un repositorio.

## Crear un repositorio nuevo de git:




</br>

~~~
git init
~~~
</br>

## Clonar un repositorio existente:

</br>

**`Ejemplo:`**

~~~
git clone repository<direcccion>

git clone https://github.com/beduExpert/DevOps-Fundamentals-2021.git
~~~

</br>

**`Nota: `** Desde nuestro repositorio en github.com podemos obtener la dirección para poder ejecutar nuestra sentencia git clone. 

![Alt text](../Ejemplo-01/assets/s2-e01-01.png?raw=true "DevOps")


</br>

---

## Flujo de Trabajo:

</br>

Tu repositorio local esta compuesto por tres "árboles" administrados por git. El primero es tu ***Directorio*** de trabajo que contiene los archivos, el segundo es el Index que actua como una zona intermedia, y el último es el ***HEAD*** que apunta al último ***commit*** realizado.

![Alt text](../Ejemplo-01/assets/s2-e01-02.png?raw=true "DevOps")

---

</br>

## Agregar y dar Commit a nuestros cambios.

</br>

Para registrar cambios (agregarlos al ***Index*** ) usando:

</br>

~~~
git add <filename>
git add .
~~~ 
</br> 
Este es el primer paso en el flujo de trabajo. Para realizar un  commit a estos cambios se utiliza:

</br>

~~~
git commit -m "Agrega un comentario relativo a tu cambio"
~~~
</br>


Ahora el archivo está incluído en el ***HEAD***, pero aún no en tu repositorio remoto.

</br>

---
## Subir tus cambios

</br>

Tus cambios están ahora en el ***HEAD*** de tu copia local. Para enviar estos cambios a tu repositorio remoto ejecuta:

</br>

~~~
git push origin master
~~~
</br>

Reemplaza  **`master`** o  **`main`**  por la rama a la que quieres enviar tus cambios.

</br>

Si no has clonado un repositorio ya existente y quieres conectar tu repositorio local a un repositorio remoto, utiliza:

</br>

~~~
git remote add origin <servidor>
~~~
</br>


Ahora podrás subir tus cambios al repositorio remoto seleccionado.

</br>

---
## Creación de ramas

</br>

Las ramas son utilizadas para desarrollar funcionalidades aisladas unas de otras. La rama master/main es la rama **"por defecto"** cuando creas un repositorio. Crea nuevas ramas durante el desarrollo y podrás fusionar el nuevo código a la rama principal.

</br>

![Alt text](..//Ejemplo-01/assets/s2-e01-03.png?raw=true "DevOps")

</br>

Crea una nueva rama llamada ***mi/rama*** y cámbiate a ella usando:

</br>

~~~
git checkout -b mi/rama
~~~
</br>


Regresa a la rama principal:

</br>

~~~
git checkout master
~~~
</br>

Eliminar nuestra rama:

</br>

~~~
git branch -d mi/rama
~~~
</br>

**`Nota:`** Una rama nueva no estará disponible para los demás, deberás subir (***push***) la rama a tu repositorio remoto.

</br>

~~~
git push origin mi/rama
~~~
</br>

---
## Actualizar y Fusionar


</br>
Para actualizar tu repositorio local al commit más nuevo, ejecuta:

</br>

~~~
git pull
~~~
</br>

En tu directorio de trabajo para bajar y fusionar los cambios remotos. Para fusionar otra rama a tu rama activa (por ejemplo ***master***), utiliza:

</br>

~~~
git merge master
~~~
</br>

En ambos casos git intentará fusionar automáticamente los cambios. Después de modificarlos, necesitas marcarlos como fusionados con:

</br>

~~~
git add miArchivo.txt
~~~
</br>

---
**`NOS VEMOS EN EL RETO 01`**
