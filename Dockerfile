FROM python:3-alpine

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY . /code
WORKDIR /code

EXPOSE 80
