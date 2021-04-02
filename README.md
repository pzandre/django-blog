# django-blog
A simple Blog-like webapp using Docker, PostgreSQL, NGinx and, of course, Django

### Initial set-up
In order to properly run the application you must run this commands to generate the environment variables.

`docker run django 'python src/manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"' > ./.env `

Later in development this method will be replaced with a shell script that will accept user inputs for the Database variables and the initial superuser data.

TODO list - Create DB variables via bash script

- [ ] POSTGRES_USER=user
- [ ] POSTGRES_PASSWORD=dbpwd
- [ ] POSTGRES_DB=db
