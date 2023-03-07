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

