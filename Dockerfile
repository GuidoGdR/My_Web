FROM python:3.12.0

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/my_web

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

COPY ./my_web .

CMD ["gunicorn", "core.wsgi:application", "-b", "0.0.0.0:8000"]