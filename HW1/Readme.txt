What is Docker? 

Docker is a popular platform for developing and deploying applications in a containerized environment. In Docker, there are two primary concepts that you should understand: Docker image and Docker container.

Docker image

A Docker image is a read-only template that contains a set of instructions for creating a Docker container. It is essentially a snapshot of the application and its dependencies, including the operating system, libraries, and other files required to run the application. Docker images are typically created using a Dockerfile, which is a text file that specifies the instructions for building the image.

Docker container

A Docker container, on the other hand, is a running instance of a Docker image. It is a lightweight and portable executable package that contains everything needed to run an application, including the application code, runtime, system tools, libraries, and settings. A Docker container can be started, stopped, and restarted without affecting the host system or other containers running on the same host.

Dockerfile

1. Start with a base image of the latest version of Ubuntu
2. Set the working directory
3. Update the package repository and install dependencies
4. Clone the Starspace repository
5. Compile Starspace
6. Changing working directory and create new directory "output"
7. Create a volume for the input file
8. Copy input file
9. Train the model on the input file and save the embeddings to the host machine
10. Command to run the Starspace program to train embeddings using the input file and save the output

# CMD /app/Starspace/starspace train -trainFile /app/input/starspace_input_file.txt -model /app/output/starspace_embeddings.txt
# CMD ["/bin/bash", "-c", "echo 'Running container'; /app/Starspace/starspace train -trainFile /app/input/starspace_input_file.txt -model /app/output/starspace_embeddings.txt && echo 'Success!'"]

#  Building the docker image called starspace
docker build -t starspace .

docker run -v /path/to/input:/app/input -v /path/to/output:/app/output starspace


docker run -v ~/ML_Engineering/HW1/volume/starspace_input_file.txt:/app/input/starspace_input_file.txt -v ~/ML_Engineering/HW1/volume:/app/output starspace

# Running the container with volume mappings with the starspace image
docker run -v ~/ML_Engineering/HW1/volume/starspace_input_file.txt:/app/input/starspace_input_file.txt -v ~/ML_Engineering/HW1/volume:/app/output starspace

