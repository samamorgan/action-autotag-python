# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /github/workspace

CMD [ "python3", "main.py" ]