# Ejemplo 1 - Archivos que para .gitignore

## Objetivos 🎯

* Familiarizarse con los archivos generados en un proyecto de Terraform.
* Ver cuales archivos ignorar en el repositorio.

## Desarrollo 📝

Extraído directamente del [.gitignore](../.gitignore) de este repositorio:

```ignore-list
# MacOS configuracion de vista de carpeta en Finder
.DS_Store

# Directorios  locales .terraform, aqui terraform descarga modulos de proveedor y otros,
# estas carpetas crece mucho en tamaño con todos los modulos de nuestros proveedores.
**/.terraform/*

# Archivos .tfstate, cuando Terraform guarda el estado localmente, otras personas
# usarán sus propios estados para sus ambientes de infra.
*.tfstate
*.tfstate.*

# Logs de fallos
crash.log
crash.*.log

# Excluir todo archivo .tfvars ya que usualmente contiene datos sensibles como:
# contraseñas, llaves privadas, y otros secretos. Que no deben ser parte de un
# repositorio, sino parte de la configuración de ambiente
*.tfvars

# Todo archivo override ya que usualmente son cambios locales
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# No agregar configuraciones personales de CLI
.terraformrc
terraform.rc
```