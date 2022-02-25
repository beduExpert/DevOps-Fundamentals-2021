# Postwork - Sesión 4
## Objetivos 🎯
1) Integrar el microservicio de esta sesión a tu proyecto `myAPI`.
2) Despliega tu proyecto para pruebas
4) Escribe nuevas funciones (rutas)
3) Pruebas en PostMan
4) Agrega un nuevo contenedor para correr Jenkins
---
## Desarrollo 📝
### <b>1) Integrar el microservicio</b>
Integra tu microservicio con su base de datos, el microservicio puede ser en tu lenguaje de preferencia, [aquí tienes](../Proyecto/python-microservice/) un ejemplo que puedes usar para basar tu propio microservicio.

Organiza tu myAPI para que cada microservicio tenga su propia base de datos (un servidor mysql puede alojar varias bases de datos) y su propio repositorio.
 
### <b>2) Despliega tu proyecto para pruebas</b>
Mediante `terraform apply`, despliega tu proyecto que ya contiene el microservicio.

### <b>3) Crea un nuevo microservicio para manejo de usuarios</b>
Escribe nuevas para crear, consultar, borrar usuarios y hacer login.

### <b>4) Agrega un nuevo contenedor para correr Jenkins</b>
Define tus nuevas peticiones en Postman para que puedas probar tu servicio nuevo.

### <b>5) Agrega un nuevo contenedor para correr Jenkins</b>
Extiende tu proyecto terraform para agregar un nuevo contenedor para correr Jenkins, exponiendo el puerto 8080.