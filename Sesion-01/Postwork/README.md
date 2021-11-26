
# Postwork 
# Sesion 01 :  Introducción al módulo de DevOps Fundamentals

🎯 **Objetivo:**

- Comprender la diferencia entre una Imagen y un Contenedor.

- Utilizar un repositorio de Imagenes Docker (Docker Hub).

- Crear tu propia Imagen Docker.

---

## ⚙️ Setup

- Asegúrate de tener instalado en tu equipo Docker

    https://docs.docker.com/engine/install/

---

## 📒 Indicaciones generales

Con base en la aplicación que has ido desarrollando a lo largo del módulo, crearás imágenes Docker y lograr versionar las mismas, tomando en cuenta las siguientes indicaciones:

- Deberás descargar y manipular imágenes Docker.

- Versionar las imágenes creadas.

- Utilizar línea de comandos para comprender la Infraestructura.

- Desplegar un servidor de aplicaciones basado en Docker.

---

## 🚀 Desarrollo.

1.- Utiliza el repo de Apache
https://hub.docker.com/_/httpd

2.- Ejecuta el comando para descargar la Imagen a tu local:

`docker pull httpd`

3.- Ejecuta el siguiente comando:

`docker images`

4.- Verás una indicación similar como la siguiente:


<pre><code>REPOSITORY      TAG       IMAGE ID       CREATED        SIZE
ubuntu-update   latest    31889a5b4786   34 hours ago   104MB
httpd           latest    ad17c88403e2   4 days ago     143MB
ubuntu          latest    ba6acccedd29   5 weeks ago    72.8MB</code></pre>

5.- Ahora, levantarás la imagen con lo siguiente:

`docker run -d --name apache-server -p 80:80 httpd`

Con esto, tendrás el servidor de aplicaciones iniciado:

![Alt text](https://raw.githubusercontent.com/beduExpert/DevOps-Fundamentals-2021/main/Sesion-01/assets/Sesion-01-16.png?raw=true "DevOps")

6.- Ejecuta lo siguiente:

`docker ps`


7.- Verás algo similar:

<pre><code>CONTAINER ID   IMAGE     COMMAND              CREATED       STATUS       PORTS                NAMES
65db7597168c   httpd     "httpd-foreground"   2 hours ago   Up 2 hours   0.0.0.0:80->80/tcp   apache-server</code></pre>

8.- Ubica el Container ID y ejecútalo:

`docker exec -it 5ec19c1e3408 bash`

9.- Una vez dentro de tu contenedor, actualiza:

`apt-get update & apt-get upgrade -y`

10.- Instala un par de tools (wget, zip)

`apt install wget`

`apt install zip`

11.- Ubícate en el path:

`cd /usr/local/apache2/htdocs`

12.- Descarga un zip, con el site a desplegar:


`wget https://github.com/beduExpert/DevOps-Fundamentals-2021/raw/main/Sesion-01/coming-soon-evening-html.zip`

13.- Descomprime el zip:

`unzip coming-soon-evening-html.zip`

14.- Actualiza el navegador, donde podrás ver el sitio actualizado como se muestra en la imagen.

![Alt text](https://raw.githubusercontent.com/beduExpert/DevOps-Fundamentals-2021/main/Sesion-01/assets/Sesion-01-17.png?raw=true "DevOps")

---

## ✅ Checklist

| Requisito      | Sí lo cumple   | No lo cumple |
| ----------- | ----------- | ----------- |
| Tener ultima version Docker en local      |        |  |
| Identificar los comandos Docker básicos   |         |  |
| Iniciar el servidor de aplicaciones    |         |  |
| Modificar la página de inicio del servidor de aplicaciones   |         |  |

---
