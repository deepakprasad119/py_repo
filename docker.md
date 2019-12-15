

# <h1> Docker Topics


# <h2> What is Docker?

Docker is an open-source lightweight containerization tool.

It helps to easily create, deploy and run application using containers.



Containerisation is bundling an application together with all it's related configuration files, libraries and dependencies.

# <h2> What is Docker image?



The Docker image is a (immutable) file used to create Docker containers.  

A docker image is made up of multiple layers. An image is composed system libraries, tools, other files and dependencies for executable code.

Every docker images are stored in the Docker registry.



# <h2> What is Docker Engine?

Docker daemon or Docker engine represents the server. 

The docker daemon and the clients can be run on the same or remote host, which can communicate through command-line client binary and full RESTful API.



# <h2> What is registry in Docker?

Docker's public registry is called Docker hub.
Docker can also have private registry.



# <h2> Commands

	docker ps 								# to see all running container

	docker run -i -t alpine /bin/bash 		# to run the image as a container


	docker info								# Information Command

	docker pull								# Download an image

	docker stats							# Container information

	Docker images							# List of images downloaded

	docker-compose -f docker-compose.json up	# to use JSON instead of YAML compose file

	docker push myorg/img					# to push the new image to Docker registry



# <h2> What are the steps for the Docker container life cycle?

Build
Pull
Run

