#!/usr/bin/env bash

if [ $1 = "django" ]; then
    sudo docker rmi barendict/django
elif [ $1 = "postgresql" ]; then
    sudo docker rmi barendict/postgresql
else
    echo "Invalid argument"
fi
