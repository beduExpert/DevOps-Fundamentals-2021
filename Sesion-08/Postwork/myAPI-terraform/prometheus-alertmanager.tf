resource docker_image "alertmanager_docker" {
  name = "prom/alertmanager"
  build {
    path = "./alertmanager-docker"
    tag  = [
      "prom/alertmanager:latest"
      ]
  }
}

# resource docker_volume "prometheus_volume" {
#   name = "prometheus_data"
# }

resource "docker_container" "alertmanager" {
  name = "alertmanager"
  image = "${docker_image.alertmanager_docker.latest}"
  privileged = true
  ports {
    internal = 9093
    external = 9093
  }
  volumes {
    volume_name = "alertmanager_data"
    host_path = "/c/Users/emile/Documents/alertmanager"
    container_path = "/alertmanager/data"
    read_only = false
  }
  # provisioner "local-exec" {
  #   command = "docker exec -d -u root jenkins chown jenkins:jenkins /var/run/docker.sock"
  # }
}

output "alertmanager_ip" { value = "alertmanager_IP=${docker_container.alertmanager.ip_address}" }