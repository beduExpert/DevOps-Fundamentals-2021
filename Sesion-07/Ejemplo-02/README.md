# Ejemplo 2 - Instalación SonarQube

## Objetivo

• Implementación de DevOps para generar automatización de flujos de testing.
• Exponer los tipos de pruebas en DevOps.

## Desarrollo

💡

Aquí se debe agregar el desarrollo del ejemplo

1. Descarga la imagen preestablecida de sonarqube

```docker pull sonarqube```
![image](https://user-images.githubusercontent.com/59855822/158932428-1b5c0ee7-6d16-4156-8ccb-cfdadb2fa809.png)

2. Descarga la imagen preestablecida de sonarqube

```docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube```

3. Utiliza el comando 
 ```docker ps -a```
para confirmar que se está ejecutando el contenedor

![image](https://user-images.githubusercontent.com/59855822/158932654-392b3998-6979-4ff2-b39e-7c74fb5a6927.png)

4. Ingresa a ```http://localhost:9000``` en tu navegador para confirmar que SonarQube ha sido cargado con éxito, recuerda que el puerto 9000 fue el que definimos, pero puedes utilizar cualquier otro puerto que esté libre en tu ordenador.

![image](https://user-images.githubusercontent.com/59855822/158933676-aff09561-2ece-448d-b65c-a82c8363e092.png)

5. Ingresa con las credenciales preestablecidas:
USUARIO: admin
CONTRASEÑA: admin

6. Al clickear el botón "LogIn" ingresarás automáticamente a otra pestaña donde podrás utilizar la contraseña que desees y clickea el botón "Update"

![image](https://user-images.githubusercontent.com/59855822/158933928-41eac99c-72ec-48a7-8068-4be352a86e31.png)

7. FELICIDADES! HAS INSTALADO SONARQUBE CORRECTAMENTE! 

![image](https://user-images.githubusercontent.com/59855822/158934040-29ef041c-e72f-49a5-9971-fe3d0a190e3a.png)

