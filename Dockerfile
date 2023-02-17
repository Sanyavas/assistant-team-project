FROM python:3.10

MAINTAINER Oleksandr Vasylyna

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app/menu.py"]

