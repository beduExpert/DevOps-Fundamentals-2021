# Reto 2 - Compila código de GitHub

## Objetivo

* Comprender empaquetado de código
* Utilidad de compilado dentro del CI/CD

## Desarrollo

Crea un pipeline tipo script SCM en el que puedas configurar un plugin maven sin necesidad de escribir código

* El pipe debe conectarse al repositorio: https://github.com/Singedpls/mvnrepository.git
* Debe compilar el código al hacer commit en la rama master
* El script path se encuentra en raíz

La integración está dada de la siguiente manera: 
![image](https://user-images.githubusercontent.com/59855822/157607354-95132396-77d2-49a0-9649-896a98db8afb.png)

TIP:
* Para que el pipe sea reconocido en tiempo menor a 30 segundos, agrega un Poll SCM con la nomenclatura: * * * * * 
![image](https://user-images.githubusercontent.com/59855822/157607891-14cf19aa-9165-4acd-b611-a7d011b73f26.png)


## Resultado

Configuración de Pipeline: 

Parte 1:
![image](https://user-images.githubusercontent.com/59855822/157607488-4f095394-2f9c-4711-a588-c2c6f3302a6f.png)

Parte 2:
![image](https://user-images.githubusercontent.com/59855822/157607575-cfdabf90-c4b8-4f08-9370-87a1425789c9.png)


![image](https://user-images.githubusercontent.com/59855822/157606614-b8c3d433-1119-414c-a09f-54e9f68e32cb.png)
