FROM python:3.10.5-slim-buster

MAINTAINER Oleksandr Vasylyna

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app/menu.py"]

#VOLUME ./data:/data
