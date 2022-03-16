# Ejemplo 1 - Comprobando comunicaciónes entre dos contenedores.

## Objetivos 🎯

* Buscar herramientas de diagnostico de red.
* Probar comunicaciones entre contenedores.

## Desarrollo 📝

Es común afrontar problemas de comunicación, donde buscamos que un contenedor se enlace con otro o comprobar el estado de tu aplicación para monitoreo.

No siempre tenemos a la mano herramientas para poder probar, pero en el dockerfile del contenedor podemos instalar las herramientas que necesitemos.

Por ejemplo, el contenedor de ejemplo que viene en la solución del postwork, trae `curl`, una herramienta para realizar peticiones http:

Abriendo una terminal interactiva al contenedor de books:

```
PS C:\Users\emile> docker exec -it -u root myapi-books /bin/bash
root@6c4629015aa0:/usr/src/books#
```
Comprobando la ubicación de `curl` con whereis:
```
root@6c4629015aa0:/usr/src/books# whereis curl
curl: /usr/bin/curl /usr/share/man/man1/curl.1.gz
```
Probando una peticion al contenedor de Jenkins via su IP interna del bridge de Docker.
```
root@6c4629015aa0:/usr/src/books# curl -v http://172.17.0.3:8080
*   Trying 172.17.0.3:8080...
* Connected to 172.17.0.3 (172.17.0.3) port 8080 (#0)
> GET / HTTP/1.1
> Host: 172.17.0.3:8080
> User-Agent: curl/7.74.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 403 Forbidden
< Date: Wed, 16 Mar 2022 07:21:29 GMT
< X-Content-Type-Options: nosniff
< Set-Cookie: JSESSIONID.74acd03b=node0grk3m9u8x1l21vepo7apv43re17.node0; Path=/; HttpOnly
< Expires: Thu, 01 Jan 1970 00:00:00 GMT
< Content-Type: text/html;charset=utf-8
< X-Hudson: 1.395
< X-Jenkins: 2.335
< X-Jenkins-Session: 1f00f901
< Content-Length: 541
< Server: Jetty(9.4.45.v20220203)
<
<html><head><meta http-equiv='refresh' content='1;url=/login?from=%2F'/><script>window.location.replace('/login?from=%2F');</script></head><body style='background-color:white; color:white;'>
...
```
Dependiendo de qué tipo de comunicación necesitaremos instalar algún programa cliente para intentar verificar conectividad con otro contenedor. Por ejemplo, si necesitamos confirmar comunicación con mysql desde el contenedor del microservicio myapi-books, podemos usar el propio cliente de python para comprobar el enlace. El siguiente código mandaría una excepción en caso de problemas de comunicación, al conectar bien simplemente termina en `exit code = 0`:
```
#!/usr/bin/env python3
import os, sys
import mysql.connector as sql

if __name__ == '__main__':
    cnx = sql.connect(
            host       =os.environ['MYSQL_IP'],
            port       =os.environ['MYSQL_PORT'],
            user       =os.environ['MYSQL_USER'],
            password   =os.environ['MYSQL_PASSWORD'],
            )
    sys.exit(0)
```