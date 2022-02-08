# Solucion al Reto

### Archivo `main.tf`
```terraform
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "3.74.1"
    }
  }
}

provider "aws" {
  # Configuration options
}
```

### En Windows cmd:
> 256,581,632 bytes
```
    ...
     Total Files Listed:
               1 File(s)    256,581,632 bytes
              20 Dir(s)  31,825,276,928 bytes free
```

### En MacOS / GitBash / Linux
> Aprox 245Mb
```
245M    .terraform/
245M    total
```