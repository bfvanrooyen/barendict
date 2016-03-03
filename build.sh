#!/usr/bin/env bash

if [ $1 = "django" ]; then
    sudo docker build -t barendict/django:latest ./docker_django
elif [ $1 = "postgresql" ]; then
    sudo docker build -t barendict/postgresql:latest ./docker_postgresql
else
    echo "Invalid argument"
fi