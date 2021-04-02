# django-blog
### **A simple Blog-like webapp using Docker, PostgreSQL and, of course, Django**
#### *by Andre Henrique Rodrigues Perez*

## Automated Linux set-up
### In order to properly run the automated you must first:

1. Verify you have Docker and Docker compose installed. Follow [this](https://docs.docker.com/get-docker/ "Get Docker") and [this](https://docs.docker.com/compose/install/ "Install Docker Compose") instructions if it is not installed.

2. You may need to also follow [this](https://docs.docker.com/engine/install/linux-postinstall/ "Post-installation steps for Linux") instructions to properly setup the Docker service.

3. Run setup.sh shell script to set the database variables.

    `$ ./setup.sh`

You'll then be prompted to enter the Database name, username and password.

This setup script was tested on a Linux environment, if you're trying to install on a different Operating System you can still set it up manually.

## Manual set-up (Windows, Mac or Linux, just for fun)
### There are also few steps to manually install the application:

1. Follow step 1 and 2 of the Automated Install above.

2. Create a file named ".env" at the root of this project (the same folder containing docker-compose.yml)

3. Using the text editor of your choice, write the following at this .env file:

`POSTGRES_DB=DATABASENAME`\
`POSTGRES_USER=USERNAME`\
`POSTGRES_PASSWORD=PASSWORD`

### **Swap DATABASENAME, USERNAME and PASSWORD with data of your choice.**

Then, using a terminal, navigate to the project folder and start the application:

`docker-compose up --build -d`

## Superuser creation
The final step is to create a Django superuser using the following command:

`docker exec -it django python src/manage.py createsuperuser`

You'll be prompted to enter an username, email and password.

This finishes the installation process and the docker containers will be running as background process. The application will be accessible entering `localhost:8000` at the web browser of your choice.

To stop the application, navigate to the project folder using a terminal and enter `docker-compose down`

To start it again simply enter `docker-compose up -d`

If you prefer to maintain the process attached to the terminal window, in order to debug, simply remove the `-d` argument from the former command.