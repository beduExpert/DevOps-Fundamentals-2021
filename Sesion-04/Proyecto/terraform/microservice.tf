resource "docker_image" "microservice" {
  name   = "microservice"
  build {
    path = "../python-microservice/."
    tag  = [
      "microservice:latest"
      ]
  }
}

resource "docker_container" "microservice" {
  image = docker_image.microservice.latest
  name  = "microservice-demo"
  ports {
    internal = 5000
    external = 5000
  }
  env = [
      "MYSQL_IP=${docker_container.mysql.ip_address}",
      "MYSQL_PORT=3306",
      "MYSQL_USER=root",
      "MYSQL_PASSWORD=abcD_1234",
      ]
  depends_on = [
    docker_image.microservice
  ]
}