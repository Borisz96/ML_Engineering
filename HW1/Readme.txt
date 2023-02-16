docker run -v /path/to/input_file:/input starspace
docker build -t starspace .


docker run -v /path/to/input:/app/input -v /path/to/output:/app/output starspace

/mle-mentoring/01_Containerization/Data/starspace_input_file.txt:/app/Data/starspace_input_file.txt -v ~/mle-mentoring/01_Containerization/Export:/app/Export 01_containerization_image
