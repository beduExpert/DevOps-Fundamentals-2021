# Solución Reto 4.

## 1 Configura el contenedor para cargar el volumen del host al del contenedor:

Desde terraform puedes enlazar estos dos paths, de esta forma el contenedor y el host comparten datos en esta ruta (socket).

Windows
```
  volumes {
    host_path = "//var/run/docker.sock"
    container_path = "/var/run/docker.sock"
    read_only = false
  }
```

Mac / Linux
```
  volumes {
    host_path = "/var/run/docker.sock"
    container_path = "/var/run/docker.sock"
    read_only = false
  }
```

---

## 2 Crea un script de provisionamiento para ajustar los permisos del socket.
Debido a que cada que docker monta el volumen se realiza bajo root, necesitamos otorgar permisos a Jenkins para que pueda escribir en el.

```
  provisioner "local-exec" {
    command = "docker exec -d jenkins chown jenkins:jenkins /var/run/docker.sock"
  }
```

Siempre que el conenedor se crea desde terraform este script se ejecuta.

---

💡 Para saber mas sobre linux sockets consulta [esta página](https://cs.uns.edu.ar/~ldm/mypage/data/rc/apuntes/introduccion_al_uso_de_sockets.pdf).