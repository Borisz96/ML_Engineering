docker run -v /path/to/input_file:/input starspace
docker build -t starspace .


CMD /app/Starspace/starspace train -trainFile /app/input/starspace_input_file.txt -model /app/output/starspace_embeddings.txt


CMD ["/bin/bash", "-c", "echo 'Running container'; /app/Starspace/starspace train -trainFile /app/input/starspace_input_file.txt -model /app/output/starspace_embeddings.txt && echo 'Success!'"]

docker run -v /path/to/input:/app/input -v /path/to/output:/app/output starspace

docker run -v ~/ML_Engineering/HW1/volume/starspace_input_file.txt:/app/input/starspace_input_file.txt -v ~/ML_Engineering/HW1/volume:/app/output starspace
