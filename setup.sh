#! /bin/bash

#This will generate the project environment variables via user's input
echo "Enter the name of your database:"
read POSTGRES_DB

if [ -z "$POSTGRES_DB" ]
  then
    echo "Database name must not be empty. Please input a valid name."
    exit 1
fi

echo "Enter your database username:"
read POSTGRES_USER

if [ -z "$POSTGRES_USER" ]
  then
    echo "Database username must not be empty. Please input a valid name"
    exit 1
fi

echo "Enter your database password:"
read -s POSTGRES_PASSWORD

if [ -z "$POSTGRES_PASSWORD" ]
  then
    echo "Database password must not be empty. Please choose a valid password"
    exit 1
fi

echo "Enter your Disqus Website Name (ONLY THE SUBDOMAIN YOU CHOSE, NOT THE .disqus.com PART --- THIS_ONE_ONLY.disqus.com)"
read -s DISQUS_WEBSITE

if [ -z "$DISQUS_WEBSITE" ]
  then
    echo "You must enter a valid Disqus Website, read the README.md file if you're lost."
    exit 1
fi

sed -i 's/DISQUS-URL/$DISQUS_WEBSITE/' src/blog/templates/article_details.html

touch ./.env

#Saving the variables at .env file
echo "POSTGRES_DB=$POSTGRES_DB" > ./.env
echo "POSTGRES_USER=$POSTGRES_USER" >> ./.env
echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> ./.env

#Building docker-compose.yml
docker-compose up --build -d
