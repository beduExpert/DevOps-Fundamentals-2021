# Postwork - Sesión 3
## Objetivos 🎯
1) Iniciar con el proyecto final `myAPI`.
2) Definir contenedor MySQL
---
## Desarrollo 📝
### 1) Iniciar con el proyecto final
Crea un nuevo repositorio GitHub con el nombre de tu preferencia. Ej: `rigo-myAPI`.

Aquí tendremos nuestros archivos de terraform y microservicios que van a componer nuestra API.

Como ejemplo, la estructura de archivos puede quedar de la siguiente forma:

```
📦rigo-myAPI
 ┣ 📂terraform
 ┃ ┗ 📄main.tf
 ┣ 📂c_mysql
 ┃ ┗ 📄dockerfile
 ┣ 📂cms_agenda_crud
 ┃ ┣ 📄dockerfile
 ┃ ┣ 📄agenda.py
 ┃ ┗ 📄requirements.txt
 ┣ 📂cms_auth
 ┃ ┣ 📄dockerfile
 ┃ ┗ 📄auth.js
 ┗ 📄README.md
 ```
 
 Donde tenemos una carpeta para los archivos de terraform y una carpeta para cada uno de nuestros contenedores / servicios. Esto facilitará la construcción de los contenedores y de terraform.

 ### 2) Define el contenedor para MySQL
 Utiliza la imágen oficial para MySQL: [Mysql / Official Image](https://hub.docker.com/_/mysql).
 Inicia un contenedor con contraseña de root en `abcD_1234` y puerto externo `3307`.
