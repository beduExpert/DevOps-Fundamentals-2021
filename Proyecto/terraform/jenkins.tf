resource "docker_image" "jenkins" {
  name = "jenkins/jenkins"
}

resource "docker_container" "jenkins" {
  name = "jenkins"
  image = "${docker_image.jenkins.latest}"
  env = [
    "JENKINS_HOME=/var/jenkins_home",
  ]
  ports {
    internal = 8080
    external = 8080
  }
  depends_on = [
    docker_image.jenkins
  ]
}

output "jenkins_ip" { value = "JENKINS_IP=${docker_container.jenkins.ip_address}" }
