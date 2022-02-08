# Ejemplo 2 - Proyecto Terraform

## Objetivo 🎯

* Identificar las partes basicas que componen un módulo de Terraform

## Desarrollo 📝

La estructura de un proyecto en Terraform (**tf**) es modular, la carpeta actual desde donde corremos tf es considerada como el módulo raíz, y este puede ejecutar otros sub módulos o módulos externos.

Al interpretar el código, Terraform fusiona todos los archivos con extensión ```.tf``` que se encuentran el la carpeta de trabajo (```pwd```) y los considera como un solo módulo, puedes referenciar recursos de un archivo en otro archivo sin necesidad de declarar una importación ya que todos estos archivos se tratan como si fuera un solo archivo.

Terraform es un lenguaje declarativo y su sintáxis básica es:

```<bloque> <tipo> <nombre> { ... }```

Por ejemplo:

```terraform
resource "aws_iam_user" "usr_mark"  {
    name = "mark@email.com"
}
```

En este ejemplo solo necesitamos un archivo, que hemos llamado: ```main.tf``` (📝 El nombre no tiene una función, puede ser el que sea), y su estructura va de la siguiente forma:

* Un bloque ```terraform```, para configurar el motor de **tf**.

```terraform
terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = ">= 2.16.0"
    }
  }
}
```

* Un bloque ```provider```, para cofigurar el proveedor

```terraform
provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}
```
* Uno o varios bloques ```resource```, ej:

```terraform
resource "docker_image" "microservice" {
  name   = "microservice"
  build {
    path = "../microservice/."
    tag  = [
      "microservice:latest"
      ]
  }
}
```

En **tf** existen otros tipos de bloques que no estamos utilizando en este ejemplo, como ```variable```, ```data```, ```module``` etc.

>💡 Usuarios MacOS:
>
> En MacOS no se necesita configurar la sección host del proveedor, comenta la línea 11 antes de iniciar.