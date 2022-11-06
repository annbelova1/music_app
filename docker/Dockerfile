FROM python:3.7.6

WORKDIR /music_app
COPY requirements.txt .

RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080