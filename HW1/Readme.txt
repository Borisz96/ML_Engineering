docker run -v /path/to/input_file:/input starspace
docker build -t starspace .


docker run -v /path/to/input:/app/input -v /path/to/output:/app/output starspace

