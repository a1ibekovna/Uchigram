FROM python:3.12-slim

WORKDIR /app

COPY requirments.txt /app/requirments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirments.txt

COPY . /app

RUN chmod +x /app/docker/django/server-entrypoint.sh