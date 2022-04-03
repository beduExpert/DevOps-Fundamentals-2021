node {
    def app
    stage('Clone') {
        checkout scm 
    }
    stage('Build') {
        app = docker.build("myapi-books:test")
    }
    stage('InitDb') {
        app.inside {
            sh 'set'
            sh 'pwd'
            sh 'pip list'
            sh 'cd src; python init-db.py;'
        }
    }
    stage('DeployTest') {
        sh 'docker stop myapi-books-test || true && docker rm myapi-books-test || true'
        sh 'docker run -p 6001:5000 -d --rm --name myapi-books-test -e MYSQL_IP="$MYSQL_IP" -e MYSQL_PORT="3306" -e MYSQL_USER="$MYSQL_USER" -e MYSQL_PASSWORD="$MYSQL_PASSWORD" myapi-books:test'
        sh 'sleep 3'
        try {
            sh 'python3 tests.py `docker inspect --format "{{ .NetworkSettings.IPAddress }}" myapi-books-test` 5000'
        }
        catch (exc) {
            throw exc
        }
        finally {
            sh 'docker stop myapi-books-test || true && docker rm myapi-books-test || true'
        }
    }
    stage('Deploy') {
        sh 'docker stop myapi-books || true && docker rm myapi-books || true'
        sh 'docker rmi myapi-books:latest'
        sh 'docker tag myapi-books:test myapi-books:latest'
        sh 'docker rmi myapi-books:test'
        sh 'docker run -p 5001:5000 -d --rm --name myapi-books -e MYSQL_IP="$MYSQL_IP" -e MYSQL_PORT="3306" -e MYSQL_USER="$MYSQL_USER" -e MYSQL_PASSWORD="$MYSQL_PASSWORD" myapi-books:latest'
        sh 'docker exec myapi-books python init-db.py'
    }
}
