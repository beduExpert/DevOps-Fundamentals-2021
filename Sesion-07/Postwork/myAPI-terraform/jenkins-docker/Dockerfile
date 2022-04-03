FROM jenkins/jenkins

USER root

# Install Docker from official repo
RUN apt-get update -qq && \
    apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-add-repository "deb [arch=$(dpkg --print-architecture)] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get update -qq && \
    apt-get install -qqy docker-ce terraform python3-distutils wget && \
    usermod -aG docker jenkins && \
    chown -R jenkins:jenkins $JENKINS_HOME/ && \
    touch /var/run/docker.sock && \
    chown -R jenkins:jenkins /var/run/docker.sock && \
    chmod 666 /var/run/docker.sock

USER jenkins

RUN cd $JENKINS_HOME && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    python3 -m pip install requests && \
    python3 -m pip list && \
    whereis python3

VOLUME [$JENKINS_HOME, "/var/run/docker.sock"]
