FROM python:3.8.10-slim-buster

WORKDIR /app

ADD ./main.py /app

ADD ./requirements.txt /app

RUN pip install -r requirements.txt

CMD python main.py