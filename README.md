# leo_demo

### What is this project
This is a Docker-based web application that serves one purpose: return the
Fibonacci number sequence, starting at 0, for a given length.

Returns 500 elements of the Fibonacci sequence
```bash
curl http://192.168.100.99:9000/500
```

### Setup

#### Virtual Box
 - Install Virtual Box for [your platform](https://www.virtualbox.org/wiki/Downloads)

#### Install Docker/Docker-Machine/Python
 - Install python 2.7
 ```bash
 brew install python
 ```
 - Install docker
 ```bash
 brew install docker
 ```
 - Install docker-machine
 ```bash
 brew install docker-machine
 ```

#### Setup docker, docker-machine
 - Create a new docker machine
 ```bash
 docker-machine create --driver virtualbox dev
 ```
 - Check your docker machine instance
 ```bash
 docker-machine ls
 ```
 - Bootstrap your CLI docker client against this new docker instance
 ```bash
 eval "$(docker-machine env dev)"
 ```

#### Build docker image
 - Run docker build
 ```bash
 docker build -t leo_web .
 ```
 - Execute the docker image
 ```bash
 docker run -it -p 9000:9000 -p 9002:9002 leo_web
 ```
 - Curl the endpoint
 ```bash
 curl http://$(docker-machine ip dev):9000/10
 ```

#### Run tests
 - On the web application
 ```bash
 pip install -r leo_web/requirements.txt
 python leo_web/app_tests.py
 ```
 - On the docker container
 Not yet defined
