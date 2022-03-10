# Reto 1 - Crea tu propio código Groovy

## Objetivo

* Comprensión de código Groovy
* Comprensión de orden de stages

## Desarrollo

Crea un pipeline llamado "devops-fundamentals" en el que puedas escribir un código en groovy con las siguientes características:

* Que sea capaz de conectarse a cualquier nodo
* Debe contener 3 stages (Docker, Build y DevOps Config)
* Los 3 stages deben tener un echo que muestre en consola para qué sirve cada uno.
* El stage DevOps Config debe nombrar y asignar variables de usuario tu nombre y contraseña "devops"
* El stage DevOps Config debe mostrar en consola tu usuario y contraseña


## Resultado


```pipeline {
    agent any

    stages {
        stage('Docker') {
            steps {
                echo 'Connecting with dockerserver-01'
            }
        }
        stage('Build') {
            steps {
                echo 'Este stage sirve para compilar el código que fue obtenido del repositorio de Git'
                echo 'Su ejecución se dio gracias a que pasó correctamente el stage de Análisis'
            }
        }
        stage('DevOps Config') {
            steps {
                echo 'Este stage sirve para conectar mediante variables de entorno, a otras herramientas de apoyo para asegurar la calidad del código'
                script{
                    env.USER_NAME = "Usuario"
                    env.USER_ID = "devops"
                }
                echo "Querido ${env.USER_NAME}"
                echo "Tu contraseña es: ${env.USER_ID}"
            }
        }
    }
}
```

![image](https://user-images.githubusercontent.com/59855822/157606045-c7303c62-aefa-4905-9dc5-52857c300fd9.png)
