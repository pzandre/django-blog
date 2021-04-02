#! /bin/bash

touch ./.env

#This will generate the project environment variables via user's input
echo "Choose the name of your database:"
read POSTGRES_DB

if [ -z "$POSTGRES_DB" -eq 0 ]
  then
    echo "Database name must not be empty. Please input a valid name."
    exit 1
fi

echo "Choose your database username:"
read POSTGRES_USER

if [ -z "$POSTGRES_USER" -eq 0 ]
  then
    echo "Database username must not be empty. Please input a valid name"
    exit 1
fi

echo "Choose your database password:"
read POSTGRES_PASSWORD

if [ -z "$POSTGRES_PASSWORD" -eq 0 ]
  then
    echo "Database password must not be empty. Please choose a valid password"
    exit 1
fi

#Saving the variables at .env file
echo "POSTGRES_DB=$POSTGRES_DB" >> ./.env
echo "POSTGRES_USER=$POSTGRES_USER" >> ./.env
echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> ./.env

#Building docker-compose.yml
docker-compose up --build -d
