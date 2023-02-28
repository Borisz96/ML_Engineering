# Start with a base image of the latest version of Ubuntu
FROM ubuntu
#22.04

# Set the working directory
WORKDIR /app
#WORKDIR /home/miki/ML_Engineering/HW1

# Update the package repository and install dependencies
RUN apt-get update && apt-get install -y \
    g++ \
    git \
    make \
    libboost-all-dev
    

# Clone the Starspace repository
RUN git clone https://github.com/facebookresearch/Starspace.git

# Compile Starspace
WORKDIR /app/Starspace
RUN make

# Changing working directory and create new directory "output"
WORKDIR /app
RUN mkdir /output

# Create a volume for the input file
#VOLUME /input

#Copy input file
#COPY ./input/starspace_input_file.txt /input/starspace_input_file.txt

# Train the model on the input file and save the embeddings to the host machine
#CMD ./starspace train \
#    -trainFile /input/starspace_input_file.txt \
#    -model modelSaveFile \
#    && cp modelSaveFile /input/starspace_embeddings.txt

# Command to run the Starspace program to train embeddings using the input file and save the output
CMD ["/bin/bash", "-c", "echo 'Running container...'; /app/Starspace/starspace train -trainFile /app/input/starspace_input_file.txt -model /app/output/starspace_embeddings.txt && echo 'Success'"]
