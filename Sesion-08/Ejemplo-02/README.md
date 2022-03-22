# Ejemplo 2 - Prometheus

## Objetivo

* Instalar, configurar y conocer sobre la herramienta de monitoreo Prometheus.

## Desarrollo

Como ya hemos visto, las bondades de Docker nos permiten instalar de manera sencilla aplicaciones que naturalmente nos llevarían más tiempo por el lenguaje de compilación, etc. Entonces, hagámos uso de Docker para nuestra instalación!

1- Al ejecutar el comando ```docker pull prom/prometheus```, automáticamente nos llevará a descargar la imagen más actual de Prometheus del Docker Hub.
    Se mostrará algo como se muestra a continuación y espera a que termine la descarga.

![image](https://user-images.githubusercontent.com/59855822/159405697-6d85b042-fb58-47c2-b2e8-2e0a950d2265.png)

2- Utiliza el comando ```docker run -p 9090 --name prometheus -v /prometheus.yml:/prometheus/prometheus.yml prom/prometheus``` para echar a andar la imagen de Prometheus.
    Recuerda que el puerto por default es el 9090, pero puedes utilizar cualquier otro que tengas libre en tu ordenador.
    Si todo salió correctamente, se mostrará al final de algunas líneas la leyenda "Server is ready to receive web requests".
    
  ![image](https://user-images.githubusercontent.com/59855822/159406230-750fd617-9c59-4e03-91b9-a971d647e6ea.png)
  
3- ¡Felicidades! Has logrado la instalación de una herramienta que está diseñado para brindar confiabilidad. Es un sistema al que cualquier usuario puede acudir durante una interrupción o incidente y diagnosticar rápidamente los problemas.

![image](https://user-images.githubusercontent.com/59855822/159406427-eb7719e7-c0f4-48e4-adae-baa60dcaa9c2.png)


    
