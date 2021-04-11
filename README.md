# django-blog
### **A simple Blog-like webapp using Docker, PostgreSQL, NGinx and, of course, Django**
#### *by Andre Henrique Rodrigues Perez*

## Automated Linux set-up
### In order to properly run the automated set-up you must first:

1. Verify you have Docker and Docker compose installed. Follow [this](https://docs.docker.com/get-docker/ "Get Docker") and [this](https://docs.docker.com/compose/install/ "Install Docker Compose") instructions if it is not installed.

2. You may need to also follow [this](https://docs.docker.com/engine/install/linux-postinstall/ "Post-installation steps for Linux") instructions to properly setup the Docker service.

3. We'll use the script made by Philipp Schmieder to create the SSL certs. 

Download the file "init-letsencrypt.sh" via [GitHub](https://github.com/wmnnd/nginx-certbot/ "Boilerplate for nginx with Let’s Encrypt on docker-compose") or using the following command:

    `curl -L https://raw.githubusercontent.com/wmnnd/nginx-certbot/master/init-letsencrypt.sh > init-letsencrypt.sh`

Open the script on any text editor and swap the example domain on line 8 with your domain and enter a valid e-mail address on line 11.

Then run `./init-letsencrypt.sh`

4. Run setup.sh shell script to set the database variables.

    `$ ./setup.sh`

You'll then be prompted to enter the Database name, username and password.

### If the application returns an error, check  with `ls -la` if the folders and subfolders inside `ssl/certbot/conf` are owned by root user. If it does, you'll have to enter `sudo chown $USER:USER *` on every subfolder. If you are unsure if you missed something, just repeat `docker-compose up` at the root folder of this project.

5. Create a Django superuser using the following command:

    `docker exec -it django python src/manage.py createsuperuser`

You'll be prompted to enter an username, email and password.

6. Run the following command:

    `docker exec -it django python src/manage.py collectstatic`

This setup script was tested on a Linux environment, if you're trying to install on a different Operating System you can still set it up manually.
