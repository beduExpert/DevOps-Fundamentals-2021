# Ejemplo 2 - Estructura de un job (stages con Groovy).

## Objetivo

* Diferenciar la importancia del orden y definir las tareas en cada stage
* Conocer el lenguaje Groovy
* Crear tu propio código en Groovy


## Desarrollo

Puedes tener tu servidor local de jenkins de manera independiente a Docker, apóyate del Jenkins War que se te compartió en la sesión 6 del prework y ejecútalo como cualquier código java "java -jar path/del/archivo"
![image](https://user-images.githubusercontent.com/59855822/157596722-6815a000-642b-45d0-ae04-b9e283a672ac.png)


Una vez logeado en http://localhost:8080 como usr: admin pass: admin
Recuerda 
* New Item
* Nombra el job y asegúrate que sea de tipo "Pipeline" y créalo.

Analiza el código, podrás observar cómo es que se inicializa y cuáles son los stages de manera muy general, así como el órden ideal de cada uno de ellos.
* Recuerda leer las línes comentadas

```pipeline {
    agent any   //conexión a cualquier nodo

    stages {    //definición para aparturar los stages
        stage('Package') {    //Primer stage
            steps{
                echo 'Obteniendo el código de Gitlab'
            }
        }
        stage('Docker') {   //Segundo stage
            steps {
                echo 'Connecting with dockerserver-01'
            }
        }
        stage('Analysis') { //Tercer stage
            steps {
                echo 'Analizar código con test del propio lenguaje de programación y alguna herramienta de análisis de código'
            }
        }
        stage('Build') {  //Cuarto stage
            steps {
                echo 'Conectando con dockerserver-01'     //El código siempre debe ser analizado, testeado y estresado antes de ser compilado y llevarlo al siguiente estado.
                echo 'Compilando código...'
            }
        }
        stage('DevOps Config') {  //Tercer stage
            environment{  //definición de variables de entorno
                ARTIFACTORY_HOME = "/ctmaster/artifactory"
            }
            steps {   //Pasos del stage 3
                echo "Conectando con herramientas externas (SonarQube, SonarCloud, Artifactory, etc.) Path: ${env.ARTIFACTORY_HOME}" //Obtiene variables con ${nombrevariable}
                script{
                    env.USER_NAME = "Singedpls"   //Nombra y asinga valor a variable
                    env.USER_ID = "123456"
                }
                echo "Querido ${env.USER_NAME}"    //Escucha de variables asignadas
                echo "El equipo ha aprovado tu cambio"
            }
        }
        stage('Promote to release') {   //También conocido como Release Candidate
            steps {
                echo 'Release Successfull...'
            }
        }
    stage('Deploy') {
            steps {
                echo 'Haciendo Deploy en servidor on-premise'   //En nuestro caso será una carpeta local
            }
        }
    }
    post{
        failure{
            emailext body: 'Theres no app to release', subject: 'Pipeline Status', to: 'pruebasdevops@gmail.com'  //envía un email de notificación si hubo fallos
        }
        success{
            emailext body: 'Build Successfull', subject: 'Pipeline Status', to: 'pruebasdevops@gmail.com'   //envía un email de notificación si no hubo fallos
        }
    }
}
```

* Guarda la configuración y ejecuta el pipeline ("build now")
* Haz click sobre cada recuadro verde y verifica que los logs han sido ejecutados correctamente.
![image](https://user-images.githubusercontent.com/59855822/157601231-ad5a0d66-4d56-43df-98d5-d05ce65744cf.png)
