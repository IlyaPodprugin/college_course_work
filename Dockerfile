# Python and Linux Version 
FROM python:3.10.0a1-alpine3.12

COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 

# Working directory
WORKDIR /app

ADD . .

CMD gunicorn coolquiz.wsgi:application --bind 0.0.0.0:$PORT