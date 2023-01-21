docker_run:
    @docker build -t awesomedate .
    @docker run -it --rm --name bot awesomedate