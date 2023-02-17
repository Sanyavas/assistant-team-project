FROM python:3.10.5-slim-buster

MAINTAINER Oleksandr Vasylyna

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app/menu.py"]

