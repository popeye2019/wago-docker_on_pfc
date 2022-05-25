# wago-docker_on_pfc
This repo will have files that can help you make your own program code, run in docker on a Wago PLC. \
Since it have been working mostly with Python code, this will be the example I will give. \
For other programming languages the procedure would be pretty much the same. \
The intention with this git repo is to give you an angle of attack for your own project with the information needed to get you up and running quickly.\
So to clearify this is NOT a complete course, but merely to show you the concopt of running your own code on the PFC.

## Steps to take:
Develop on your PC and test on a Raspberry Pi.                        ( its easier this way ) \
Convert the project to run on a Wago PFC and upload to docker hub     ( so you can pull the image to your PFC later on ) \
Pull your docker image to the PFC and run it.

# Lines that will help you do the work
## Build images for testing on your Raspberry Pi (or similar)
In order to run your program in a container, you must build the program images first, with the help of a Dockerfile

### Structure of dockerfile
FROM python       \
WORKDIR /app      \
COPY . /app/      \
EXPOSE 80         \
CMD ["python", "myPythonprogram.py"]

### Build the image
Go to the dir where you have your Dockerfile and your python script and run the line underneath

docker build -t myTag .

### Run the program in a container with this line
docker run --rm myTag \
or \
docker run --rm 78ce2f690466

--rm will remove the container after container stop \
--it interactive in case you need to interact with the program, like inputs fx. \
-p port numbers - could be -p 8080:80 (hostport:containerport) \
-d daemon mode - if you wish to run the program in the background. This way the terminal will not be blocked but you will no see messages from the running container either.

## Make code compatible with the Wago PFC and PUSH
docker buildx build --platform linux/arm/v7 -t yourdockerusername/yourdockerrepo:repoversion --push .

this is and example: "docker buildx build --platform linux/arm/v7 -t dannyolsen/wago-docker_on_pfc:latest --push ."

if you want to make your program available for other architectures "--platform linux/amd64,linux/arm64,linux/arm/v7" can be used in the line above

## Running the Docker image on the PFC
When running the line below, if the image is not present on the PFC it will be downloaded first and run afterwards \
docker run -p port:port containername

this is and example: "docker run --rm --name myContainer myTag"
