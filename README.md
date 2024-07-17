# Videoflix

My little project is a Netflix Dummy. Thats have a FE NX Angular project, Django BE in a Docker Container, Postgresql und redis in a container.

## Introduction

1. pull the project

    ```bash
    git clone git@github.com:JohnTwiiX/videoflix.git
    ```

1. build frontend

    ```bash
    npm i -g nx
    cd Frontend
    nx build videoflix # serve with nx serve videoflix
    ```

1. create network

    ```bash
    docker network create <your-network>
    ```

1. run postgres container

    ```bash
    docker run &&\
        --name <name> &&\
        --network <your-network> &&\
        -e POSTGRES_PASSWORD=<password> &&\
        -e POSTGRES_USER=<user> &&\
        -e POSTGRES_DB=<db-name> &&\
        -d postgres 
    ```

1. run redis container

    ```bash
    docker run && \
        -d && \
        --name <name> && \
        --network <your-network> && \
        -e REDIS_PASSWORD=<password>
        -p 6379:6379 && \
        bitnami/redis:latest
    ```

1. create your .env

    ```bash
    cd Backend/videoflix
    cp simple.env .env
    ```

1. build docker image

    ```bash
    cd Backend
    docker build -t videoflix:0.0.0.1 .
    ```

1. run your backend container

    ```bash
    docker run && \
        --name <name> && \
        --network <your-network> && \
        -p <your-port>:8000 && \
        --restart on-failure && \
        <your-image> 
    ```
