FROM python:3.6-stretch

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD ["uwsgi", "app.ini"]