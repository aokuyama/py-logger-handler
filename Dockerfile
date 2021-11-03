FROM python:3.7-alpine

ENV PYTHONIOENCODING utf-8
WORKDIR /app

RUN pip install requests
