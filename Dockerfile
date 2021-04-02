FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python src/manage.py shell -c \
    "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" \
    | grep SECRET_KEY >> ./.env