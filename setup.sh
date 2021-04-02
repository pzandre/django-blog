#! /bin/bash

touch ./.env

#This will generate the project environment variables via user's input
echo "Choose the name of your database:"
read POSTGRES_DB
echo "Choose your database username:"
read POSTGRES_USER
echo "Choose your database password:"
read POSTGRES_PASSWORD

#Saving the variables at .env file
echo "POSTGRES_DB=$POSTGRES_DB" >> ./.env
echo "POSTGRES_USER=$POSTGRES_USER" >> ./.env
echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> ./.env

#Building docker-compose.yml
docker-compose up --build -d

