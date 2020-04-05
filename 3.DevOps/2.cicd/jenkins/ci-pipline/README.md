# Pipeline

This is a ci/cd pipeline which allows you to build and test your projects automatically after commiting code to your repository. Moreover, you can deploy the containerized pipeline on a staging server.
For changing the stages, you do not need to change the pipline itself, but you only have to change the Jenkinsfile in the root directory of the repository. There are three predefined stages for the pipline, "build stage", "test stage", "deploy stage", which you can change them as you wish or you can add stages as many as you want.

This project is a docker container based on jenkins.

---
## To run the pipe line for the first time

```sh
sudo docker run \
	-u root \
	-d \
	-p 8080:<desired_port>
	-p 50000:50000 \
	-v $HOME/jenkins-data:/var/jenkins_home \
	-v /var/run/docker.sock:/var/run/docker.sock \
	<ImageID>
```

## To watch the running pipline and finding the containerID

```sh
sudo docker ps -a
```

## To access jenkins
In the browser, enter the IP address of the server which jenkins is running on, via the port which you have provided as the "desired\_port" above.

## To authenticate for the first time as admin
For the first time, you have to authenticate with a key to use jenkins. Since jenkins runs inside a docker container as a detached container (because of the "-d" flag), you have to see the key in the logs via:

```sh
sudo docker logs <containerID>
```
then you should enter the password which is provided in the log, in browser.

## To stop/start the pipe line

```sh
sudo docker start <ContainerID>
```

---
## To remove the pipline container

```sh
sudo docker rm <ContainerID>
```

** Note: changes to pipeline will not be saved unless you export the docker container to an image for later usage.
So do not forget to export it before removing the container. **

## To export the docker 

```sh
sudo docker commit <containerID> author/image:version
```

---
## To build the new pipline with the Dockerfile

```sh
sudo docker build -t author/name:version .
```

Note: After editing docker pipline and building the container, some dangling pipeline may pollute the docker image directory and consume storage. To remove dangling images:
sudo docker rmi $(sudo docker images -f "dangling-true" -q)

## For garbage collection

```sh
sudo docker container prune #for containers
sudo docker image prune #for images
```
