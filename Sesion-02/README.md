## Flujos de DevOps y manejo de código 🤖
---



### En ciclo de vida de desarrollo de software se muestra en la siguiente imagen

![Alt text](../Sesion-02/assets/1.png?raw=true "DevOps")



Una vez que ya tenemos el código albergado en un repositorio compartido, la herramienta que recomendamos utilizar  es una herramienta distribuida de control de versiones como Git, desearíamos, como una meta ideal, disponer de un mecanismo de integración continua y de despliegue continuo, es decir, poder realizar entregas a entornos productivos que sean muy rápidas y en corto espacio de tiempo.

</br>



Para ello, una vez que ya tenemos nuestro desarrollo finalizado, lo empaquetamos, lo hacemos disponible para poder testarlo, gestionamos la configuración y finalmente hacemos un despliegue en un entorno productivo.



</br>

Cabe mencionar que en el ciclo de desarrollo tambien podemos tener como herramienta de apoyo, por ejemplo herramientas de Jira Etc.

![Alt text](../Sesion-02/assets/2.png?raw=true "DevOps")

</br>

Necesitaríamos alguna de estas  herramienta que nos ayude a gestionar las diferentes versiones de código, como Git o Subversion, aunque recomendamos utilizar Git, porque es una herramienta que ofrece mejores prestaciones, mucha agilidad y otra serie de ventajas.

</br>

Como ya hemos comentado, una vez que hemos codificado, volvemos a empaquetar y hacemos el testeo de la aplicación.
Nos apoyamos en otro tipo de herramientas para generar ese empaquetado, al que después podemos hacer despliegue, como por ejemplo TestLink, Bamboo o Jenkins, serian una buena opcion de trabajo.


 Como dato importante debemos entender que GIT es el SCV (sistema de control de versiones) de código abierto más utilizado que te permite rastrear los cambios realizados en los archivos y nos ayuda a colaborar en el desarrollo de software y aplicaciones ya que un proyecto GIT consta de tres secciones principales: el directorio de trabajo, el área de preparación y el directorio git.

</br>
Una vez que ya tenemos el empaquetado listo para hacer un despliegue a producción, podremos utilizar herramientas tipo Ansible, que automatizan esa labor de despliegue y si combinamos ese empaquetado, que ya tenemos de nuestra aplicación, para gestionarlo en un entorno basado en contenedores Docker o con un orquestador encima, por ejemplo Kubernetes, podríamos tener un entorno de integración continua en el que los despliegues, es decir, el acto del deploy, fuese aún más rápido.

---


</br>




<span style="color:orange"> <ins>Manejo de codigo</ins> </span>
---




Estos son unos comandos básicos de GIT que debes conocer:

</br> 

•	<span style="color:green">*git init* </span>creará un nuevo repositorio local GIT. El siguiente comando de Git creará un repositorio en el directorio actual:

~~~
git init
~~~

</br> 

•	Como alternativa, puedes crear un repositorio dentro de un nuevo directorio especificando el nombre del proyecto:


</br>

~~~
git init [nombre del proyecto]
~~~

</br>

•	
<span style="color:green">*git clone* </span>se usa para copiar un repositorio. Si el repositorio está en un servidor remoto, usa:
</br>

~~~
git clone nombredeusuario@host:/path/to/repository
~~~
</br>

•	A la inversa, ejecuta el siguiente comando básico para copiar un repositorio local:

</br>

~~~
git clone /path/to/repository
~~~
</br>

•	
<span style="color:green">*git add* </span>se usa para agregar archivos al área de preparación. Por ejemplo, el siguiente comando de Git básico indexará el archivo temp.txt:

</br>

~~~
git add <temp.txt>
~~~
</br>

•	
<span style="color:green">*git commit* </span>creará una instantánea de los cambios y la guardará en el directorio git.

</br>

~~~
git commit –m “El mensaje que acompaña al commit va aquí”
~~~
</br>



<span style="color:red">*•	Ten en cuenta que los cambios confirmados no llegarán al repositorio remoto.* </span>
</br>



•	<span style="color:green">*git config* </span>puede ser usado para establecer una configuración específica de usuario, como el email, nombre de usuario y tipo de formato, etc. Por ejemplo, el siguiente comando se usa para establecer un email:

</br>

~~~
git config --global user.email devops@bedu.org
~~~
</br>


•	La opción <span style="color:green">*--global* </span>   le dice a GIT que vas a usar ese correo electrónico para todos los repositorios locales. Si quieres utilizar diferentes correos electrónicos para diferentes repositorios, usa el siguiente comando:

</br>

~~~
git config --local user.email devops@bedu.org
~~~
</br>


•	<span style="color:green">*git status* </span>muestra la lista de los archivos que se han cambiado junto con los archivos que están por ser preparados o confirmados.

</br>

~~~
git status
~~~
</br>


•	<span style="color:green">*git push* </span>se usa para enviar confirmaciones locales a la rama maestra del repositorio remoto. Aquí está la estructura básica del código:

</br>

~~~

git push  origin <master>
~~~
</br>

###	
<span style="color:grey">*Reemplaza <master> con la rama en la que quieres enviar los cambios cuando no quieras enviarlos a la rama maestra.* </span>

</br>

•	<span style="color:green">*git checkout* </span>crea ramas y te ayuda a navegar entre ellas. Por ejemplo, el siguiente comando crea una nueva y automáticamente se cambia a ella:

</br>

~~~
command git checkout -b <nombre de la rama>
~~~
</br>


•	<span style="color:grey">*Para cambiar de una rama a otra, sólo usa:* </span>


</br>

~~~
git checkout <nombre de la rama>
~~~
</br>

•	<span style="color:green">*git remote* </span>te permite ver todos los repositorios remotos. El siguiente comando listará todas las conexiones junto con sus URL's:

</br>

~~~
git remote -v
~~~
</br>


•	<span style="color:grey">*Para conectar el repositorio local a un servidor remoto, usa este comando:* </span>


</br>

~~~
git remote add origin  <direccion URL>
~~~
</br>

•	<span style="color:grey">*Por otro lado, el siguiente comando borrará una conexión a un repositorio remoto especificado:* </span>

</br>

~~~

git remote <nombre-del-repositorio>
~~~
</br>

•	<span style="color:green">*git branch* </span>se usa para listar, crear o borrar ramas. Por ejemplo, si quieres listar todas las ramas presentes en el repositorio, el comando debería verse así:

</br>

~~~
git branch
~~~
</br>

•	<span style="color:grey">*Si quieres borrar una rama, usa:* </span>


</br>

~~~
 git branch -d <nombre de la rama>
~~~
</br>

•	<span style="color:green">*git pull* </span>fusiona todos los cambios que se han hecho en el repositorio remoto con el directorio de trabajo local.

</br>

~~~
git pull
~~~
</br>

•	<span style="color:green">*git merge* </span>se usa para fusionar una rama con otra rama activa:

</br>

~~~
git merge <nombre de la rama>
~~~
</br>

•	<span style="color:green">*git diff* </span>se usa para hacer una lista de conflictos. Para poder ver conflictos con respecto al archivo base, usa:

</br>

~~~
git diff --base <nombre del archivo>
~~~
</br>
•	<span style="color:grey">*El siguiente comando se usa para ver los conflictos que hay entre ramas antes de fusionarlas:*</span>


</br>

~~~
git diff <rama origen> <rama destino>
~~~
</br>


•	<span style="color:grey">*Para ver una lista de todos los conflictos presentes usa:* </span>


</br>

~~~
git diff
~~~
</br>

•	<span style="color:green">*git tag* </span>marca commits específicos. Los desarrolladores lo usan para marcar puntos de lanzamiento como v1.0 y v2.0.

</br>

~~~
git tag 1.1.0 <insertar el ID commit>

~~~
</br>

•	<span style="color:green">*git log* </span>se usa para ver el historial del repositorio listando ciertos detalles de la confirmación. Al ejecutar el comando se obtiene una salida como ésta:

</br>

~~~
commit 15f4b6c44b3c8344caasdac9e4be13246e21sadw
Author: Bedu DevOps <devops@bedu.org>
Date:   Wed Dec 1 12:00:00 2021 -0600
~~~
</br>

•	<span style="color:green">*git reset* </span>sirve para resetear el index y el directorio de trabajo al último estado de confirmación.

</br>

~~~
git reset - -hard HEAD
~~~
</br>


•	<span style="color:green">*git rm* </span>se puede usar para remover archivos del index y del directorio de trabajo.

</br>

~~~
git rm filename.txt
~~~
</br>

•	<span style="color:green">*git stash* </span>guardará momentáneamente los cambios que no están listos para ser confirmados. De esta manera, pudes volver al proyecto más tarde.

</br>

~~~
git stash
~~~
</br>

•	<span style="color:green">*git show* </span>se usa para mostrar información sobre cualquier objeto git.

</br>

~~~
git show
~~~
</br>

•	<span style="color:green">*git fetch* </span>le permite al usuario buscar todos los objetos de un repositorio remoto que actualmente no se encuentran en el directorio de trabajo local.

</br>

~~~
git fetch origin
~~~
</br>

•	<span style="color:green">*git ls-tree* </span>te permite ver un objeto de árbol junto con el nombre y modo de cada ítem, y el valor blob de SHA-1. Si quieres ver el HEAD, usa:

</br>

~~~
git ls-tree HEAD
~~~
</br>



•	<span style="color:green">*git cat-file* </span>se usa para ver la información de tipo y tamaño de un objeto del repositorio. Usa la opción -p junto con el valor SHA-1 del objeto para ver la información de un objeto específico, por ejemplo:

</br>

~~~
git cat-file –p d670460b4b4aece5915caf5c68d12f560a9fe3e4
~~~
</br>

•	<span style="color:green">*git grep* </span>le permite al usuario buscar frases y palabras específicas en los árboles de confirmación, el directorio de trabajo y en el área de preparación. Para buscar por bedu.org en todos los archivos, usa:

</br>

~~~
git grep “bedu.org”
~~~
</br>

•	<span style="color:green">*git grep gitk*</span>  muestra la interfaz gráfica para un repositorio local. Simplemente ejecuta:
</br>

~~~

gitk
~~~
</br>


•	<span style="color:green">*git instaweb*</span> te permite explorar tu repositorio local en la interfaz GitWeb. Por ejemplo:

</br>

~~~
git instaweb –http=webrick
~~~
</br>

•	<span style="color:green">*git gc*</span> limpiará archivos innecesarios y optimizará el repositorio local.

</br>

~~~
git gc
~~~
</br>

•	<span style="color:green">*git archive*</span> le permite al usuario crear archivos zip o tar que contengan los constituyentes de un solo árbol de repositorio. Por ejemplo:
</br>

~~~
git archive - -format=tar master
~~~
</br>

•	<span style="color:green">*git prune*</span> elimina los objetos que no tengan ningún apuntador entrante.

</br>

~~~
git prune
~~~ 
</br>

•	<span style="color:green">*git fsck*</span> realiza una comprobación de integridad del sistema de archivos git e identifica cualquier objeto corrupto


</br>

~~~
git fsck
~~~
</br>

•	<span style="color:green">*git rebase*</span> se usa para aplicar ciertos cambios de una rama en otra. Por ejemplo:

</br>

~~~
git rebase master
~~~
</br>

---

## Implementar un flujo con Git-Flow.

<span style="color:orange">*¿Cómo funciona GitFlow?.*</span>



</br>
La imagen que se muestra a continuacion nos muestra  ventajas y desvantajas de GitFlow

</br>

![Alt text](../Sesion-02/assets/3.png?raw=true "DevOps")


<span style="color:pink">*👍 Ventajas:*</span>

1.	Alienta el uso de pull request.

2.	Control estricto de los cambios, porque normalmente solo algunos desarrolladores estan autorizados para aprobar los pull request.

3.	Después de entender como funciona, es simple de utilizar.

</br>

<span style="color:pink">*👎 Desventajas:*</span>

1.	Los primeros 2 beneficios también se convierten en contras, porque el tener tanto control del proceso alienta y crea dependencia de una persona o varias personas encargadas al momento revisar los cambios, en algunos casos puede llegar a convertirse en micro-management.

2.	El crear branches de larga vida (long-living branches), puede provocar que cuando necesitemos unificar (mergear) el código se creen muchos conflictos sobre todo en equipos que están desarrollando una misma sección.  Por ejemplo Supongamos que se va a crear el branch de release para que se le empiecen a realizar pruebas, por otra parte, el equipo debe seguir desarrollando funcionalidades que no son parte del release y se continua integrando código al branch de develop, creando así 2 lineas de "tiempo" (develop y release).


1.	No permite hacer un release de código rápido. Imaginemos que por error, reparamos un bug en el branch equivocado o  se integro al branch equivocado (siguiendo el flujo normal) vamos a tener que volver a crear un pull request, esperar al review, el build, correr los tests, etc., este paso costara tiempo ⏳ o  bien simplemente si queremos agarrar lo que se ha desarrollado y hacer un release inmediatamente, no es posible, es muy probable que el código no se encuentre listo para hacerlo.

</br>

![Alt text](../Sesion-02/assets/4.png?raw=true "DevOps")

---
## Implementar un flujo con Trunk-based development

</br>

Un  trunk-based development es una estrategia de Git donde existe un trunk(un branch principal, usualmente llamado master/main) en el cual todo el equipo colabora he integra directamente (hace push), siguiendo estas consideraciones:

</br>

1. No existen branches de larga duración. no se le da mantenimiento a ningún branch. (si fuese necesario crearlo) y se encuentra un error, el mismo debe ser reparado en el trunk y luego se haría un nuevo branch de release, pero nunca se le da mantenimiento a ese branch. 

</br>


- <span style="color:Yellow">*Nota:*</span> En algunos casos es permitido hacer cherry-pick para mover un cambio, o hacerlo directo en el branch de release, pero se debe de mover inmediatamente al branch de develop.

</br>

2. Se debe hacer commit al menos una vez al día (esto no significa que vamos integrar cualquier código solo por hacer commit esto lo que busca es eliminar la distancia entre los desarrolladores cuando se empieza a codear cosas nuevas. muchas veces se desarrolla código que alguien más ya había hecho en su branch pero no lo había subido.

3.	Todo lo que se le haga commit es código funcional, esto implica que se cumpla la definición de hecho (definition of done), se hayan creado las pruebas necesarias y todo lo que sea requerido para asegurarse que el código no esta introduciendo un bug 🐛. 
4.	El trunk siempre debe encontrarse en un estado verde y optimo es decir listo para hacerle release.

![Alt text](../Sesion-02/assets/5.png?raw=true "DevOps")

</br>

<span style="color:orange">*Desarrollo basado en troncos (Trunk based development ) y la revisión de código o pull request.*</span> 


Esta  metodología anima que haya más programacion entre parejas (pair programming) y no tener que hacer pull requests. En la versión escalada (scaled trunk based development) para equipos más grandes, se permite crear branches de tiempo corto(que no vivan mas de un día) hacerles code review y sean integrados rápidamente.

![Alt text](../Sesion-02/assets/6.png?raw=true "DevOps")

</br>

Lo importante de este tema es identificar la diferencia más grandes entre GitFlow y Trunk Based Development se encuentra en el scope (ambito) del desarrollo de una nueva funcionalidad, en GitFlow se espera que el desarrollador dure días, semanas hasta meses en entregar su tarea completa, diferente a Trunk Based development en que espera que se entreguen porciones de código pequeñas y se integradas rápidamente al trunk. Existen diferentes "sabores" o modificaciones de esta estrategia, pero el objetivo es el mismo.

</br>
Trunk based development nos permite ser más efectivos y versátiles al momento de hacer releases, pero a su vez requiere que el equipo proporcione automatización que certifique que nuestro código esta en el estado optimo para ser liberado.


</br>

---
**`NOS VEMOS EN EL POSTWORD`**


