# Using Python-Charmers via Docker

This directory contains [`Dockerfile`](Dockerfile) to make it easy to get up and running with Python-Charmers via [Docker](http://www.docker.com/).

## Installing Docker

General installation instructions are [on the Docker site](https://docs.docker.com/installation/), but we give some quick links here:

- [OSX](https://docs.docker.com/installation/mac/): [docker toolbox](https://www.docker.com/toolbox)
- [ubuntu](https://docs.docker.com/installation/ubuntulinux/)

## Running the container

I prepared [`Makefile`](Makefile) to simplify docker commands within make commands.

- Build the container and start a Jupyter Notebook
    ```sh
    $ make notebook
    ```
- Build the container and start an iPython shell
    ```sh
    $ make ipython
    ```
- Build the container and start a bash
    ```sh
    $ make bash
    ```
- Mount a volume for external data sets
    ```sh
    $ make DATA=~/mydata
    ```
- Prints all make tasks
    ```sh
    $ make help
    ```