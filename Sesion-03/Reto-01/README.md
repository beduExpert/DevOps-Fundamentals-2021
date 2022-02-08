# Reto 1 - Obtén el uso de disco del proveedor de AWS.

## Objetivo 🎯

* Evaluar el uso en disco de un proveedor mayor.

## Desarrollo 📝

* Crea una nueva carpeta para proyecto de **tf**: `mkdir aws-tf`.
* Cambia tu carpeta de trabajo a la nueva carpeta: `cd aws-tf`.
* Crea un archivo `main.tf` con el proveedor de AWS.
* Inicializa Terraform: `terraform init`.
* Ejecuta el comando para obtener el uso en disco:
    * Windows cmd: `dir /s .terraform`
    * MacOS, GitBash y Linux: `du -shc .terraform`

Comparte tus resultados con el instructor.

> 💡 [Solución](./resp.md).
