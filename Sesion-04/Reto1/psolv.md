## Propuesta solucion:

Algunas alternativas, pero una que es sencilla y segura:
Debido a que Docker instala un puente de red y podemos iniciar contenedores con interfaces de red que funcionan dentro de ese espacio de ip. Al iniciar un contenedor en modo bridge, docker por defecto nos asigna una IP en el rango de red del puente, una especie de red virtual. Todos los contenedores con una ip de ese rango pueden comunicarse aislados del host real.

```
Ejemplo
Contenedor 1:       Contenedor 2:
(app)               (mysql)
172.17.0.1    ->    172.16.0.2:3306
```

⚠️ Donde el puerto 3306 es el valor interno del contenedor, no el puerto que se expone al host.

---
📝 Detalles sobre los tipos de comunicaciones en Docker:
[Understanding Docker Networks and resolving conflict with Docker Subnet IP Range!](https://medium.com/codebrace/understanding-docker-networks-and-resolving-conflict-with-docker-subnet-ip-range-bfaad092a7ea)