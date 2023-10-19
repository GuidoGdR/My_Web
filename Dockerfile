FROM python:3.12.0

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app/my_web

RUN mkdir -p /usr/src/app/data/media
RUN mkdir /usr/src/app/data/sqlite

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

COPY ./my_web .

