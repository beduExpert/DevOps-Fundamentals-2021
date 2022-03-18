# Ejemplo 1 - Navegación Docker

## Objetivo

* Agregar los objetivos del ejemplo (Mínimo agregar 2 objetivos y Borrar está linea una vez se hay leido)

## Desarrollo
NOTA: Recuerdo que para todos los casos, puedes utilizar ```--help``` para orientarte en caso de tener alguna duda específica, escritura para ejecución de comandos, etc.
![image](https://user-images.githubusercontent.com/59855822/158926513-f89bf6c4-c0d2-442e-a7e1-bf2a6e12a392.png)

1. Inicializa la herramienta Docker Desktop y utiliza el comando ```docker ps -a``` para conocer las imágenes que tienes descargadas 
![image](https://user-images.githubusercontent.com/59855822/158924075-0657ab2c-a01d-4996-aa29-cfe1d57bf262.png)
Intenta el mismo proceso con el comando ```docker container ls``` y observarás que ambas tienen la misma utilidad y dan la misma información.
Recuerda que las imagenes Docker son plantillas (que incluyen una aplicación, los binarios y las librerias necesarias) que se utilizan para construir contenedores Docker y ejecutarlos (los contenedores ejecutarán una imagen previamente compilada). También podemos decir que las imagenes Docker son instancias de un contenedor.

2. Para crear una imagen a partir de un Dockerfile, utiliza el comando 
 ```docker build <path>```
 Puede existir el caso donde es un directorio interno o bien, que deseas obtener del repositorio público en internet, para dicho caso, esta es la manera correcta:
 ```docker build https://github.com/docker/rootfs.git#container:docker```

3. Para eliminar una imagen, utiliza el comando: 
  ```docker rm [OPTIONS] CONTAINER [CONTAINER...]```
Para ejemplos de usos de este comando, consulta la sección de ejemplos a continuación.
--force , -f		  Forza remover el contenedor corriendo
--link , -l		    Elimina el link especificado
--volumes , -v		Elimina volúmenes anónimos asociados al contenedor
Por ejemplo, si estás seguro de eliminar y no quieres una segunda verificación, agrega -f a la ejecución:
```docker rm nombreimagen -f```
En lugar del nombre de la imagen, también puedes utilizar el CONTAINER ID!

4. Inicia un contenedor:
```docker run [OPTIONS] IMAGE [COMMAND] [ARG...]```
El comando primero crea una capa de contenedor grabable sobre la imagen especificada y luego la inicia usando el comando especificado.

5. Buscar imágenes del repositorio oficial de Docker (Docker Hub)
``` docker search [OPTIONS] TERM```

6. Arrancar un contenedor
``` docker start <mi_contenedor>```

7. Detener mi contenedor
``` docker stop <mi_contenedor>```

8. Mostrar Imágenes Docker
``` docker images```
El listado que aparezca será únicamente con las imágenes dentro de tu espacio Docker, puedes verificarlo con el ambiente gráfico.
![image](https://user-images.githubusercontent.com/59855822/158927124-e436dcd6-cf58-45a0-b6fb-a8a149c188c1.png)

9. Crear una etiqueta TARGET_IMAGE que haga referencia a SOURCE_IMAGE
``` docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]```
Un nombre de imagen se compone de componentes de nombre separados por barras, opcionalmente con el prefijo de un nombre de host de registro. El nombre de host debe cumplir con las reglas estándar de DNS, pero no puede contener guiones bajos. Si hay un nombre de host, opcionalmente puede ir seguido de un número de puerto en el formato: 8080. Si no está presente, el comando utiliza el registro público de Docker ubicado en registration-1.docker.io de forma predeterminada. Los componentes del nombre pueden contener letras minúsculas, dígitos y separadores. Un separador se define como un punto, uno o dos guiones bajos o uno o más guiones. Un componente de nombre no puede comenzar ni terminar con un separador.

10. Conocer la versión de Docker con la que se está trabajando
``` docker version```

11. Actualizar versión de Docker a la última disponible
``` docker update```


