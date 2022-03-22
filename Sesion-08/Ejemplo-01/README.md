# Ejemplo 1 - Grafana

## Objetivo

* Instalar, configurar y conocer sobre la herramienta de monitoreo Grafana.

## Desarrollo

Como ya hemos visto, las bondades de Docker nos permiten instalar de manera sencilla aplicaciones que naturalmente nos llevarían más tiempo por el lenguaje de compilación, etc. Entonces, hagámos uso de Docker para nuestra instalación!

1- Al ejecutar el comando ```docker pull grafana/grafana```, automáticamente nos llevará a descargar la imagen más actual de Grafana del Docker Hub.
    Se mostrará algo como se muestra a continuación y espera a que termine la descarga.
    
![image](https://user-images.githubusercontent.com/59855822/159402549-dc41fea1-3847-4b69-8926-6a319835fd36.png)

2- Utiliza el comando ```docker run -d --name=grafana -p 3000:3000 grafana/grafana``` para echar a andar la imagen de Grafana.
    Recuerda que el puerto por default es el 3000, pero puedes utilizar cualquier otro que tengas libre en tu ordenador.
    Si todo salió correctamente, únicamente mostrará el id del contenedor como se muestra a continuación: 

![image](https://user-images.githubusercontent.com/59855822/159403217-58294350-9dd9-4457-b620-f1a82fb3f06a.png)

3. Revisa en la ventana del Docker Desktop que el contenedor haya corrido correctamente con el puerto y ruta elegidos.

![image](https://user-images.githubusercontent.com/59855822/159403417-ba93a68f-793c-4c01-ad46-aaabac99465d.png)

4. Ingresa con tu navegador a ```http://localhost:3000/login``` y podrás observar que el ambiente de Grafana se encuentra en tu ordenador.

![image](https://user-images.githubusercontent.com/59855822/159403740-18499a0e-a712-4e0e-beff-a5b9f367df11.png)

Utiliza las credenciales *Usuario*: admin Contraseña: admin
    
    
    
