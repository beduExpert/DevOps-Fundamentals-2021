resource docker_image "prometheus_docker" {
  name = "prom"
  build {
    path = "./prometheus-docker"
    tag  = [
      "prom:latest"
      ]
  }
}

# resource docker_volume "prometheus_volume" {
#   name = "prometheus_data"
# }

resource "docker_container" "prometheus" {
  name = "prometheus"
  image = "${docker_image.prometheus_docker.latest}"
  privileged = true
  ports {
    internal = 9090
    external = 9090
  }
  volumes {
    host_path = "//var/run/docker.sock"
    container_path = "/var/run/docker.sock"
    read_only = false
  }
  volumes {
    volume_name = "prometheus_data"
    host_path = "/c/Users/emile/Documents/prometheus_data"
    container_path = "/prometheus-data"
    read_only = false
  }
  provisioner "local-exec" {
    command = "docker exec -d -u root jenkins chown jenkins:jenkins /var/run/docker.sock"
  }
}

output "prometheus_ip" { value = "PROMETHEUS_IP=${docker_container.prometheus.ip_address}" }