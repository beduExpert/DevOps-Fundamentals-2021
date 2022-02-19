resource "docker_image" "mysql" {
  name = "mysql:8"
}

resource "docker_container" "mysql" {
  name = "mysql"
  image = "${docker_image.mysql.latest}"
  env = [
    "MYSQL_ROOT_PASSWORD=abcD_1234"
  ]
  ports {
    internal = 3306
    external = 3307 # Usar un puerto no estandard
  }
  depends_on = [
    docker_image.mysql
  ]
}

output "ip" { value = "MYSQL_IP=${docker_container.mysql.ip_address}" }
