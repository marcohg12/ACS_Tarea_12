# ACS_Tarea_12

## File Descriptions

The file called 'Dockerfile' contains the configurations used to build a Docker image of the application. This file is used to build a Docker image of the application that will be pushed to Docker Hub, so that it can be later used to build a Docker container.

The file called 'python-ci.yml' contains the configurations of the continuous integration pipeline using GitHub Actions. It contains two jobs, one for building and testing the application, and other used to build the application (using the 'Dockerfile') and then push the Docker image to Docker Hub.
